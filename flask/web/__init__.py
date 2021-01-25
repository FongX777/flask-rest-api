import os
from flask import Flask, request
import mysql.connector
from mysql.connector import Error
from web.use_case.ListTasksUseCase import ListTasksUseCase
from web.use_case.CreateTaskUseCase import CreateTaskUseCase
from web.use_case.UpdateTaskUseCase import UpdateTaskUseCase
from web.use_case.DeleteTaskUseCase import DeleteTaskUseCase
from web.dao.TaskDAO import MySQLTaskDAO

app = Flask(__name__)


def get_cursor():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'web'
    }
    try:
        return mysql.connector.connect(**config).cursor()
    except Error as e:
        print('Cannot connect to db', e)
        raise Exception('Not connected to db')


def get_conn():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'web'
    }
    try:
        return mysql.connector.connect(**config)
    except Error as e:
        print('Cannot connect to db', e)
        raise Exception('Not connected to db')


@app.route('/')
def index():
    # Use os.getenv('key') to get environment variables
    app_name = os.getenv('APP_NAME')

    if app_name:
        return f'Hello from {app_name} running in a Docker container behind Nginx'

    return 'Hello from Flask'


@app.route('/tasks')
def list_all_tasks():
    taskDAO = MySQLTaskDAO(get_conn())
    use_case = ListTasksUseCase(taskDAO)
    return use_case.execute()


@app.route('/task', methods=['POST', 'PUT'])
def post_task():
    taskDAO = MySQLTaskDAO(get_conn())
    if request.method == 'POST':
        use_case = CreateTaskUseCase(taskDAO)
        return use_case.execute(request.json['name'])

    else:
        use_case = UpdateTaskUseCase(taskDAO)
        return use_case.execute(request.json['id'], request.json['name'], request.json['status'])


@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    taskDAO = MySQLTaskDAO(get_conn())
    use_case = DeleteTaskUseCase(taskDAO)
    use_case.execute(int(id))
    return ''
