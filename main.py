import csv

MAX_STUDENTS = 5

# Read mentors and add student count
mentors = {}
with open("data/mentors.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        mentor_id, mentor_career = row
        mentors[mentor_id] = {"career": mentor_career, "count": 0}

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
    for mentor_id, mentor in mentors.items():
        if mentor["count"] < MAX_STUDENTS and mentor["career"] == student["interest"]:
            pairings.append([student["id"], mentor_id])
            mentors[mentor_id]["count"] += 1
            assigned = True
            break
    if not assigned:
        unassigned_students.append(student)

# Handle unassigned students
for student in unassigned_students:
    for mentor_id, mentor in mentors.items():
        if mentor["count"] < MAX_STUDENTS:
            pairings.append([student["id"], mentor_id])
            mentors[mentor_id]["count"] += 1
            break

# Output pairings
with open("data/pairings.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(pairings)
