from web.domain.task import Task, TaskStatus


def to_task_dto(task: Task):
    return {"id": task.id, "name": task.name, "status": task.status.value}


def create_task(taskDAO, name: str):
    task = taskDAO.add_task(name, TaskStatus.INCOMPLETE)
    return to_task_dto(task)


def update_task(taskDAO, id: int, name: str, status: int):
    task = taskDAO.get(id)  # type: Task
    if task is None:
        return None
    task.update(name, TaskStatus(status))
    updated_task = taskDAO.update_task(task)
    return to_task_dto(updated_task)
