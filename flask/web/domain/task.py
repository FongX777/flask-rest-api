from enum import Enum


class TaskStatus(Enum):
    INCOMPLETE = 0
    COMPLETE = 1


class Task:
    def __init__(self, id: int, name: str, status: TaskStatus):
        self.id = id
        self.name = name
        self.status = status

    def update(self, name: str, status: TaskStatus):
        self.name = name
        self.status = status
