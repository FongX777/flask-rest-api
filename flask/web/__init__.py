import os
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from web.use_case.list_tasks import ListTasksUseCase
from web.use_case.use_cases import create_task, update_task
from web.use_case.delete_task import DeleteTaskUseCase
from web.dao.task import MySQLTaskDAO

app = Flask(__name__)


def get_cursor():
    config = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'database': os.getenv('DB_DATABASE'),
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
def route_list_all_tasks():
    taskDAO = MySQLTaskDAO(get_conn())
    use_case = ListTasksUseCase(taskDAO)
    return use_case.execute()


@app.route('/task', methods=['POST'])
def route_post_task():
    if 'name' not in request.json or not isinstance(request.json['name'], str):
        return jsonify({'message': 'Invalid name'}), 400

    taskDAO = MySQLTaskDAO(get_conn())
    result = create_task(taskDAO, request.json['name'])
    return jsonify(result), 201


@app.route('/task/<id>', methods=['PUT'])
def route_put_task_by_id(id):
    if 'name' not in request.json or not isinstance(request.json['name'], str):
        return jsonify({'message': 'Invalid name'}), 400

    if 'status' not in request.json or not isinstance(request.json['status'], int):
        return jsonify({'message': 'Invalid status'}), 400

    taskDAO = MySQLTaskDAO(get_conn())
    id = int(id)
    result = update_task(
        taskDAO, id=id, name=request.json['name'], status=request.json['status'])
    if result is None:
        return jsonify({'message': 'Task not exists'}), 404
    return jsonify(result), 200


@app.route('/task/<id>', methods=['DELETE'])
def route_delete_task(id):
    taskDAO = MySQLTaskDAO(get_conn())
    use_case = DeleteTaskUseCase(taskDAO)
    use_case.execute(int(id))
    return '', 200
