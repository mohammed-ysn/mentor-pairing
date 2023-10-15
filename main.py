import csv
import generate_data
import student
import mentor

# Maximum students per mentor
MAX_STUDENTS = 5

generate_data.reset("data")

students = student.read("data/students.csv")
mentors, mentor_queues = mentor.read("data/mentors.csv")

# Pair students and mentors
pairings: list[list[str]] = [["Student ID", "Mentor ID", "Career Strand"]]
unassigned_students: list[dict[str, str]] = []

for student in students:
    assigned = False

    if student["interest"] in mentor_queues:
        min_mentor: str = mentor_queues[student["interest"]].get()[1]

        count = int(mentors[min_mentor]["count"])
        if count < MAX_STUDENTS:
            pairings.append([student["id"], min_mentor, student["interest"]])
            updated_count = count + 1
            mentors[min_mentor]["count"] = updated_count
            assigned = True

            mentor_queues[student["interest"]].put((updated_count, min_mentor))

    if not assigned:
        unassigned_students.append(student)

# Handle unassigned students
for student in unassigned_students:
    pairings.append([student["id"], "unassigned", student["interest"]])

# Output pairings
with open("data/pairings.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(pairings)

print("Pairing complete")
