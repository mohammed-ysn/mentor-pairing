import csv

from participant import pair_students_with_mentors, read_participants

if __name__ == "__main__":
    students = read_participants("data/students.csv", "student")
    mentors = read_participants("data/mentors.csv", "mentor")

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
