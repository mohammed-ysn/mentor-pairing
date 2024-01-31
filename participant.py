import csv
from dataclasses import dataclass, field
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
        participants = set()
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
            participants.add(participant)

    return participants


def parse_help_type(help_type):
    help_types = help_type.split(";")
    return {ht.strip() for ht in help_types}
