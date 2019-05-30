""" structures.py implementation of the queue """

from typing import List, Any
from datetime import datetime

class Job:
    """ Data Structure which stores information about jobs inserted. """

    def __init__(self, name: str, faculty: int, role: int, status: int, desc: str):
        self._name: str = name
        self._faculty: str = faculty
        self._role: str = role
        self._status: int = status
        self._desc: str = desc
        self._complete: bool = False
        self._date = datetime.now()
        # self._info: List = {self._name, self._role, self._status, self._faculty, self._complete}
        self.__todb__(self._name, self._faculty, self._role, self._status, self._desc, self._date, self._complete)

    def __todb__(self, name: str, faculty: int, role: int, status: int, description: str, date: Any, complete: bool) -> None:
        """ Insert into a DB """
        # should return the primary_key
        return None

    def update(self, id: int) -> None:
        """ Update info in DB and change completion status. """
        return None

class Queue:
    """ Queueing system: First In First Out. """

    def __init__(self, wait_time: int):
        self._QUEUE: List = []
        self._wait_time: int = wait_time

    def enqueue(self, job):
        self._QUEUE.append(job)

    def dequeue(self, id: int):
        if self.__size__() < 1:
            return None
        else:
            self._QUEUE.pop(0)

    def __size__(self):
        return len(self._QUEUE)
