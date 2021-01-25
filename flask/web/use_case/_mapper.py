from web.domain.task import Task


def to_task_dto(task: Task):
    return {"id": task.id, "name": task.name, "status": task.status.value}
