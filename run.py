""" Entry point of program """

from UTILS.structures import Job
from UTILS.structures import Queue
from UTILS.structures import DATES
from datetime import datetime
from typing import Type

q: Type[Queue] = Queue()

def insert(name: str, faculty: int, role: int, status: int, desc: str, date: DATES):
    job = Job(name, faculty, role, status, desc, date)
    index = job.todb()
    q.enqueue(job)
    print(index)


def main():
    insert("Paula Poe", 2, 2, 1, "dafsda", datetime.now())


if __name__ == "__main__":
    main()