import pytest
from web.domain.task import Task, TaskStatus
from web.use_case.use_cases import create_task, update_task, delete_task, list_tasks
from web.dao.task import MySQLTaskDAO


class FakeTaskDAO(MySQLTaskDAO):
    __tasks = None
    __counter = 1

    def __init__(self):
        self.__tasks = {}

    def getTasks(self):
        return self.__tasks

    def get(self, id: int):
        return self.__tasks[id]

    def get_tasks(self):
        return list(self.__tasks.values())

    def add_task(self, name, status: TaskStatus):
        id = self.__counter
        self.__tasks[id] = Task(id=id, name=name, status=status)
        self.__counter += 1
        return self.__tasks[id]

    def update_task(self, id, name, status):
        self.__tasks[id] = Task(id=id, name=name, status=status)
        return self.__tasks[id]

    def delete_task(self, id):
        self.__tasks.pop(id)


def test_create_task_should_return_the_task():
    taskDAO = FakeTaskDAO()
    taskDTO = create_task(taskDAO, 'name')
    assert taskDTO['name'] == 'name'


def test_create_task_should_persist_a_new_task():
    taskDAO = FakeTaskDAO()
    create_task(taskDAO, 'name')
    assert taskDAO.getTasks()[1].name == 'name'


def test_get_task_should_return_task_list():
    taskDAO = FakeTaskDAO()
    taskDAO.add_task('wash dishes', TaskStatus(0))
    taskDAO.add_task('throw garbage', TaskStatus(0))
    taskDAO.add_task('sleep', TaskStatus(0))

    taskDTOs = list_tasks(taskDAO)
    assert len(taskDTOs) == 3


def test_update_task_should_return_task():
    taskDAO = FakeTaskDAO()
    taskDAO.add_task('wash dishes', TaskStatus(0))
    taskDTO = update_task(taskDAO, 1, 'do homework', 1)

    assert taskDTO['name'] == 'do homework'
    assert taskDTO['status'] == 1


def test_delete_task_should_return_the_task():
    taskDAO = FakeTaskDAO()
    taskDAO.add_task('wash dishes', TaskStatus(0))
    delete_task(taskDAO, 1)

    assert len(taskDAO.getTasks().values()) == 0
