from enum import Enum


class Task:
    def __init__(self, id: int, name: str, status: int):
        self.id = id
        self.name = name
        self.status = status

    def update(self, name: str, status: int):
        self.name = name
        self.status = status


class TaskStatus(Enum):
    INCOMPLETE = 0
    COMPLETE = 1
