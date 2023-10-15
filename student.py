import csv


def read(path):
    # List of students with their id and career interest
    students: list[dict[str, str]] = []

    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            student_id: str
            career_interest: str
            student_id, career_interest = row

            students.append({"id": student_id, "interest": career_interest})

    return students
