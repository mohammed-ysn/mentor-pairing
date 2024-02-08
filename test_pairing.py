from participant import (
    generate_random_mentors,
    generate_random_students,
    pair_students_with_mentors,
)

students = generate_random_students(50)
mentors = generate_random_mentors(10)

pairings, unassigned_students, unassigned_mentors = pair_students_with_mentors(
    students, mentors
)

print("Pairing complete")
for student, mentor in pairings.items():
    print(f"S: '{student.full_name}' M:'{mentor.full_name}' IND: '{mentor.industry}'")

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
