from web.domain.task import Task, TaskStatus
from typing import TYPE_CHECKING


def to_task_dto(task: Task):
    return {"id": task.id, "name": task.name, "status": task.status.value}


def create_task(taskDAO, name: str):
    task = taskDAO.add_task(name, TaskStatus.INCOMPLETE)
    return to_task_dto(task)


def update_task(taskDAO, id: int, name: str, status: int):
    task = taskDAO.get(id)
    if task is None:
        return None
    task.update(name, TaskStatus(status))
    updated_task = taskDAO.update_task(task.id, task.name, task.status.value)
    return to_task_dto(updated_task)


def delete_task(taskDAO, id: int):
    taskDAO.delete_task(id)


def list_tasks(taskDAO):
    tasks = taskDAO.get_tasks()

    return list(map(to_task_dto, tasks))
