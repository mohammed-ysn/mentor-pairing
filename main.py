import csv
from heapq import heappop, heappush

from mentor import read as read_mentors
from student import read as read_students


def pair_students_with_mentors(students, mentors):
    pairings = {}
    unassigned_students = set(students)
    unassigned_mentors = set(mentors)

    all_industries = set(
        [student.interest for student in students]
        + [mentor.industry for mentor in mentors]
    )
    # Queue for every industry
    # Key: industry
    # Value: priority queue of mentors
    mentor_queues = {
        # Initialise empty queues for each industry
        industry: []
        for industry in all_industries
    }

    # Populate queues with mentors
    for mentor in mentors:
        heappush(mentor_queues[mentor.industry], (custom_cmp(mentor), mentor))

    # Iterate through students and pair them with mentors
    for student in students:
        # Get the queue for the student's industry
        mentor_queue = mentor_queues[student.interest]

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
                unassigned_mentors.remove(mentor)

                # Push the mentor back into the queue if they can take more students
                if mentor.current_num_students < mentor.max_students:
                    heappush(mentor_queue, (custom_cmp(mentor), mentor))

                break

    return pairings, unassigned_students, unassigned_mentors


def custom_cmp(mentor):
    return (mentor.current_num_students, mentor.id)


if __name__ == "__main__":
    students = read_students("data/students.csv")
    mentors = read_mentors("data/mentors.csv")

    pairings, unassigned_students, unassigned_mentors = pair_students_with_mentors(
        students, mentors
    )

    # Output pairings to csv
    with open("data/pairings.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Student", "Mentor", "Industry", "Student Email", "Mentor Email"]
        )
        for student, mentor in pairings.items():
            writer.writerow(
                [
                    student.full_name,
                    mentor.full_name,
                    mentor.industry,
                    student.email,
                    mentor.email,
                ]
            )

    print("Pairing complete (see data/pairings.csv)")

    # Print the pairings
    for student, mentor in pairings.items():
        print(
            f"S: '{student.full_name}' M:'{mentor.full_name}' IND: '{mentor.industry}'"
        )

    # Handle unassigned students if needed
    if unassigned_students:
        print()
        print("Unassigned students:")
        for student in unassigned_students:
            print(f"{student.full_name} ({student.interest})")

    if unassigned_mentors:
        print()
        print("Unassigned mentors:")
        for mentor in unassigned_mentors:
            print(f"{mentor.full_name} ({mentor.industry})")
