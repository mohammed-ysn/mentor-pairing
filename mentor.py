import csv
from queue import PriorityQueue


def read(path):
    # Map mentor id to a dict with career strand and count of students
    mentors: dict[str, dict[str, int | str]] = {}
    # Map career strand to a priority queue of mentors
    # Priority is based on the number of students assigned to the mentor
    mentor_queues: dict[str, PriorityQueue[tuple[int, str]]] = {}

    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            mentor_id: str
            mentor_career: str
            mentor_id, mentor_career = row

            mentors[mentor_id] = {"career": mentor_career, "count": 0}

            if mentor_career not in mentor_queues:
                mentor_queues[mentor_career] = PriorityQueue()

            mentor_queues[mentor_career].put((0, mentor_id))

    return mentors, mentor_queues
