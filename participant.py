import csv
from collections import defaultdict
from dataclasses import dataclass, field
from heapq import heappop, heappush
from itertools import count
from typing import Set


@dataclass
class Participant:
    id_generator = count(1)

    id: int
    full_name: str
    email: str
    help_type: Set[str] = field(default_factory=set)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.id == other.id


@dataclass
class Student(Participant):
    interest: str = ""

    def __hash__(self):
        return super().__hash__()


@dataclass
class Mentor(Participant):
    industry: str = ""
    max_students: int = 0
    current_num_students: int = 0

    def __hash__(self):
        return super().__hash__()


def read_participants(path, participant_type):
    with open(path) as f:
        reader = csv.DictReader(f)
        participants = []
        for row in reader:
            if participant_type == "student":
                participant = Student(
                    id=next(Student.id_generator),
                    full_name=row["Full name"].strip(),
                    email=row["Username"].strip(),
                    interest=row["Desired industry"].strip(),
                    help_type=parse_help_type(
                        row["What types of support are you seeking from alumni?"]
                    ),
                )
            elif participant_type == "mentor":
                participant = Mentor(
                    id=next(Mentor.id_generator),
                    full_name=row["Full name"].strip(),
                    email=row["Email address"].strip(),
                    industry=row["Industry"].strip(),
                    help_type=parse_help_type(
                        row["Types of career help you would like to provide"]
                    ),
                    max_students=int(
                        row["How many students would you be willing to mentor?"]
                    ),
                )
            participants.append(participant)

    return participants


def parse_help_type(help_type):
    help_types = help_type.split(";")
    return {ht.strip() for ht in help_types}


def pair_students_with_mentors(students, mentors):
    pairings = {}
    unassigned_students = set(students)
    unassigned_mentors = set(mentors)

    # Key: industry, Value: priority queue of mentors
    mentor_queues = defaultdict(list)

    # Populate queues with mentors
    for mentor in mentors:
        heappush(mentor_queues[mentor.industry], (custom_cmp(mentor), mentor))

    # Iterate through students and pair them with mentors
    for student in students:
        # Get the queue for the student's industry
        mentor_queue = mentor_queues[student.interest]

        # Temporarily store mentors that are unsuitable for the student
        unsuitable_mentors = []

        # Iterate through the queue until a mentor is found
        while mentor_queue:
            (_, mentor) = heappop(mentor_queue)
            if (
                student.interest == mentor.industry
                # Check that student and mentor have at least one help type in common
                and student.help_type & mentor.help_type
            ):
                pairings[student] = mentor
                mentor.current_num_students += 1
                unassigned_students.remove(student)
                unassigned_mentors.discard(mentor)

                # Push the mentor back into the queue if they can take more students
                if mentor.current_num_students < mentor.max_students:
                    heappush(mentor_queue, (custom_cmp(mentor), mentor))

                break

            # If the mentor is unsuitable, temporarily store them to be added back to the queue
            unsuitable_mentors.append(mentor)

        # Add the unsuitable mentors back into the queue
        for mentor in unsuitable_mentors:
            heappush(mentor_queue, (custom_cmp(mentor), mentor))

    return pairings, unassigned_students, unassigned_mentors


def custom_cmp(mentor):
    return (mentor.current_num_students, mentor.id)
