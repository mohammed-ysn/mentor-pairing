import os
import csv


def gen():
    # Define the data for mentors and students
    mentors_data = [
        [1, "Engineering"],
        [2, "Medicine"],
        [3, "Law"],
        [4, "Engineering"],
        [5, "Medicine"],
        [6, "Computer Science"],
    ]

    students_data = [
        [101, "Engineering"],
        [102, "Engineering"],
        [103, "Medicine"],
        [104, "Medicine"],
        [105, "Law"],
        [106, "Computer Science"],
        [107, "Engineering"],
        [108, "Engineering"],
        [109, "Engineering"],
        [110, "Medicine"],
    ]

    # Create the 'data' directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Write mentors data to mentors.csv
    with open("data/mentors.csv", mode="w", newline="") as mentors_file:
        mentors_writer = csv.writer(mentors_file)
        mentors_writer.writerows(mentors_data)

    # Write students data to students.csv
    with open("data/students.csv", mode="w", newline="") as students_file:
        students_writer = csv.writer(students_file)
        students_writer.writerows(students_data)

    print(
        "CSV files 'mentors.csv' and 'students.csv' have been created in the 'data' directory."
    )
