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
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'database': os.getenv('DB_DATABASE'),
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
