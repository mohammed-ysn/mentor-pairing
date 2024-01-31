import csv
from dataclasses import dataclass, field
from itertools import count
from typing import Set


@dataclass
class Student:
    id_generator = count(1)

    id: int
    full_name: str
    email: str
    interest: str
    help_type: Set[str] = field(default_factory=set)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.id == other.id


def read(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        students = set()
        for row in reader:
            student = Student(
                id=next(Student.id_generator),
                full_name=row["Full name"].strip(),
                email=row["Username"].strip(),
                interest=row["Desired industry"].strip(),
                help_type=parse_help_type(
                    row["What types of support are you seeking from alumni?"]
                ),
            )
            students.add(student)

    return students


def parse_help_type(help_type):
    help_types = help_type.split(";")
    return {ht.strip() for ht in help_types}
