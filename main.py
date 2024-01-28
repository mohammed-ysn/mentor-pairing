import csv
from heapq import heappop, heappush

from mentor import read as read_mentors
from student import read as read_students


def pair_students_with_mentors(students, mentors):
    pairings = {}
    unassigned_students = set(students)
    mentor_queue = []

    # Initialise the mentor queue based on max_students
    for mentor in mentors:
        heappush(mentor_queue, (mentor.max_students, mentor))

    # Iterate through students and pair them with mentors
    for student in students:
        while mentor_queue:
            max_students, mentor = heappop(mentor_queue)
            if (
                max_students > 0
                and student.interest == mentor.industry
                # Check that student and mentor have at least one help type in common
                and student.help_type & mentor.help_type
            ):
                pairings[student] = mentor
                mentor.max_students -= 1
                unassigned_students.remove(student)
                heappush(mentor_queue, (mentor.max_students, mentor))
                break

    return pairings, unassigned_students


if __name__ == "__main__":
    students = read_students("data/students.csv")
    mentors = read_mentors("data/mentors.csv")

    pairings, unassigned_students = pair_students_with_mentors(students, mentors)

    # Output pairings to csv
    with open("data/pairings.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Student", "Mentor"])
        for student, mentor in pairings.items():
            writer.writerow([student.full_name, mentor.full_name])

    print("Pairing complete")

    # Handle unassigned students if needed
    if unassigned_students:
        print("Unassigned students:")
        for student in unassigned_students:
            print(student.full_name)
