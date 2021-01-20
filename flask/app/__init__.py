from flask import Flask, request
from app.use_case.ListTasksUseCase import ListTasksUseCase
from app.use_case.CreateTaskUseCase import CreateTaskUseCase
from app.use_case.UpdateTaskUseCase import UpdateTaskUseCase
from app.use_case.DeleteTaskUseCase import DeleteTaskUseCase
from app.dao.TaskDAO import TaskDAO
import os

flaskApp = Flask(__name__)


taskDAO = TaskDAO()


@flaskApp.route('/tasks')
def list_all_tasks():
    use_case = ListTasksUseCase(taskDAO)
    return use_case.execute()


@flaskApp.route('/task', methods=['POST', 'PUT'])
def post_task():
    if request.method == 'POST':
        use_case = CreateTaskUseCase(taskDAO)
        return use_case.execute(request.json['name'])
    else:
        use_case = UpdateTaskUseCase(taskDAO)
        return use_case.execute(request.json['id'], request.json['name'], request.json['status'])


@flaskApp.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    use_case = DeleteTaskUseCase(taskDAO)
    use_case.execute(int(id))
    return ''
