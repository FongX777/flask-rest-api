import mysql.connector
from mysql.connector import Error


def run_sql(sql):
    config = {
        'user': 'root',
        'password': 'root',
        'host': '0.0.0.0',
        'port': '3306',
        'database': 'web'
    }
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute(sql)
        results = []
        for (id, name, status) in cursor:
            results.append({"id": id, "name": name, "status": status})
        return results
    except Error as e:
        print('Cannot connect to db', e)
        raise Exception('Not connected to db')
    finally:
        cursor.close()
        connection.close()


class TaskDAO(object):
    __db = None
    __cursor = None
    __counter = 1

    def __init__(self, cursor):
        self.__db = {}
        self.__cursor = cursor

    def getTasks(self):
        # self.__cursor.execute("SELECT id, name, status from tasks")
        return list(self.__db.values())

    def insertTask(self, name):
        id = (self.__counter)
        self.__db[id] = {"id": id, "name": name, "status": 0}
        self.__counter += 1
        # return self.__db[id]
        return run_sql("SELECT id, name, status FROM tasks;")

    def updateTask(self, id, name, status):
        self.__db[(id)]["name"] = name
        self.__db[(id)]["status"] = status
        return self.__db[id]

    def deleteTask(self, id):
        if ((id) in self.__db):
            self.__db.pop((id))
