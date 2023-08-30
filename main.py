import csv
from queue import PriorityQueue

MAX_STUDENTS = 5

# Read mentors and add to priority queues
mentors = {}
mentor_queues = {}

with open("data/mentors.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        mentor_id, mentor_career = row
        mentors[mentor_id] = {"career": mentor_career, "count": 0}

        if mentor_career not in mentor_queues:
            mentor_queues[mentor_career] = PriorityQueue()

        mentor_queues[mentor_career].put((0, mentor_id))

# Read students
students = []

with open("data/students.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        student_id, career_interest = row
        students.append({"id": student_id, "interest": career_interest})

# Pair students and mentors
pairings = []
unassigned_students = []

for student in students:
    assigned = False

    if student["interest"] in mentor_queues:
        min_mentor = mentor_queues[student["interest"]].get()[1]

        if mentors[min_mentor]["count"] < MAX_STUDENTS:
            pairings.append([student["id"], min_mentor, student["interest"]])
            mentors[min_mentor]["count"] += 1
            assigned = True

        mentor_queues[student["interest"]].put(
            (mentors[min_mentor]["count"], min_mentor)
        )

    if not assigned:
        unassigned_students.append(student)

# Handle unassigned students
for student in unassigned_students:
    pairings.append([student["id"], "unassigned", student["interest"]])

# Output pairings
with open("data/pairings.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(pairings)
