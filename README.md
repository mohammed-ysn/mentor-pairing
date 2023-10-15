# Mentor Pairing

This program, developed for the Cambridge University Islamic Society, is designed to pair potential mentors with mentees.

## Data Schema

### Mentors (`data/mentors.csv`)

Each row in the CSV represents a mentor.

The CSV has the following columns:
- `mentor_id`: A string representing the mentor's ID.
- `mentor_career`: A string representing the mentor's career strand.

### Students (`data/students.csv`)

Each row in the CSV represents a student.

The CSV has the following columns:
- `student_id`: A string representing the student's ID.
- `career_interest`: A string representing the student's career interest.

## Pairing Process

1. The program reads data from CSV files for mentors and students.
2. It pairs students with mentors based on their career interests and ensures that the number of students assigned to a mentor does not exceed the `MAX_STUDENTS` value.
3. Unassigned students are handled at the end.
4. The final pairings are exported to a CSV file.
