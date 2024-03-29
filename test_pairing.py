import random
import string

from participant import Mentor, Student, pair_students_with_mentors

with open("industries.txt", "r") as f:
    industries = tuple(line.strip() for line in f)

with open("help_types.txt", "r") as f:
    help_types = tuple(line.strip() for line in f)


def generate_random_students(num_students):
    students = set()
    for i in range(num_students):
        students.add(
            Student(
                id=next(Student.id_generator),
                full_name=f"Student {i+1}",
                email=generate_random_email(),
                interest=random.choice(industries),
                help_type=set(
                    random.sample(help_types, random.randint(1, len(help_types)))
                ),
            )
        )
    return students


def generate_random_mentors(num_mentors):
    mentors = set()
    for i in range(num_mentors):
        mentors.add(
            Mentor(
                id=next(Mentor.id_generator),
                full_name=f"Mentor {i+1}",
                email=generate_random_email(),
                industry=random.choice(industries),
                help_type=set(
                    random.sample(help_types, random.randint(1, len(help_types)))
                ),
                max_students=random.randint(1, 5),
            )
        )
    return mentors


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com"]
    username = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10))
    )
    domain = random.choice(domains)
    return f"{username}@{domain}"


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
