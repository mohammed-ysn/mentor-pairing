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
        print(f"{student.full_name} ({student.interest}) [help: {student.help_type}]")

if unassigned_mentors:
    print()
    print("Unassigned mentors:")
    for mentor in unassigned_mentors:
        print(f"{mentor.full_name} ({mentor.industry}) [help: {mentor.help_type}]")

# Print capacity filled
print()
print("Capacity filled:")
for mentor in mentors:
    print(
        f"{mentor.full_name} ({mentor.industry}) - {mentor.current_num_students}/{mentor.max_students}"
    )
print(
    "Total capacity filled:",
    sum(mentor.current_num_students for mentor in mentors),
    "/",
    sum(mentor.max_students for mentor in mentors),
)
