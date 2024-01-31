import csv
from dataclasses import dataclass, field
from itertools import count
from typing import Set


@dataclass
class Mentor:
    id_generator = count(1)

    id: int
    full_name: str
    email: str
    industry: str
    max_students: int
    help_type: Set[str] = field(default_factory=set)
    current_num_students: int = 0

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, Mentor):
            return False
        return self.id == other.id


def read(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        mentors = set()
        for row in reader:
            mentor = Mentor(
                id=next(Mentor.id_generator),
                full_name=row["Full name"].strip(),
                email=row["Email address"].strip(),
                industry=row["Industry"].strip(),
                help_type=parse_help_type(
                    row["Types of career help you would like to provide"]
                ),
                max_students=int(
                    row["How many students would you be willing to mentor?"]
                ),
            )
            mentors.add(mentor)

    return mentors


def parse_help_type(help_type):
    help_types = help_type.split(";")
    return {ht.strip() for ht in help_types}
