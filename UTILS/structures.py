""" structures.py implementation of the queue """

from dataclasses import dataclass
from typing import List, NewType, Tuple, Type
from datetime import datetime
from UTILS.db import DB

DATES = NewType('DATES', datetime.now())
db = DB()
conn = db.get_connection()


@dataclass
class Job:
    """ Data Structure which stores information about jobs inserted. """
    name: str
    faculty: int
    role: int
    status: int
    desc: str
    complete: bool = False
    date: DATES = datetime.now()

    def todb(self) -> int:
        """ Insert into a DB & return PK"""
        try:
            cursor = conn.cursor()
            query: str = "INSERT INTO JOB (NAME, FACULTY_ID, ROLE_ID, STATUS_ID, TODAY, DESCRIPTION, COMPLETE) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING ID;" # noqa
            data: Tuple = (self.name, self.faculty, self.role, self.status, self.date, self.desc, self.complete)  # noqa
            cursor.execute(query, data)
            conn.commit()
            return cursor.fetchone()[0]
        except RuntimeError:
            raise RuntimeError("Could not inser into TABLE JOB.")

    def set_id(self, id: int) -> None:
        self._id = id

    def update(self, id: int) -> None:
        """ Update info in DB and change completion status. """
        try:
            cursor = conn.cursor()
            query: str = "UPDATE JOB SET COMPLETE = (%s) WHERE ID = (%s)"
            data: Tuple = (True, id)
            cursor.execute(query, data)
            conn.commit()
        except RuntimeError:
            raise RuntimeError("Record doesnot exist.")


class Queue:
    """ Queueing system: First In First Out. """

    def __init__(self):
        self._QUEUE: List[Type[Job]] = list()

    def enqueue(self, job: Type[Job]) -> None:
        self._QUEUE.append(job)

    def dequeue(self, id: int) -> None:
        if self.__size__() < 1:
            return None
        else:
            self._QUEUE.pop(0)

    def __size__(self) -> int:
        return len(self._QUEUE)
