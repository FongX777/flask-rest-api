import mysql.connector
from mysql.connector import Error


class AbstractTaskDAO:
    __db = None
    __counter = 1

    def __init__(self):
        self.__db = {}

    def getTasks(self):
        return list(self.__db.values())

    def insertTask(self, name):
        id = (self.__counter)
        self.__db[id] = {"id": id, "name": name, "status": 0}
        self.__counter += 1
        return self.__db[id]

    def updateTask(self, id, name, status):
        self.__db[(id)]["name"] = name
        self.__db[(id)]["status"] = status
        return self.__db[id]

    def deleteTask(self, id):
        if ((id) in self.__db):
            self.__db.pop((id))


class MySQLTaskDAO:
    __db = None
    __conn = None
    __counter = 1

    def __init__(self, conn):
        self.__db = {}
        self.__conn = conn

    def getTasks(self):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, name, status FROM tasks;")
        tasks = []
        for (id, name, status) in cursor:
            tasks.append({"id": id, "name": name, "status": status})
        cursor.close()
        return tasks

    def insertTask(self, name, status):
        cursor = self.__conn.cursor()
        sql = "INSERT INTO tasks (name, status) VALUES (%s, %s)"
        cursor.execute(sql, (name, status))
        self.__conn.commit()
        id = cursor.lastrowid
        cursor.execute(
            "SELECT id, name, status FROM tasks WHERE id = %s", (id,))
        data = cursor.fetchone()
        task = {"id": data[0], "name": data[1], "status": data[2]}
        cursor.close()
        return task

    def updateTask(self, id, name, status):
        print('~~~~~~`', id, name, status)
        cursor = self.__conn.cursor()
        sql = "UPDATE tasks SET name = %s, status = %s WHERE id = %s;"
        cursor.execute(sql, (name, status, id))
        self.__conn.commit()
        cursor.execute(
            "SELECT id, name, status FROM tasks WHERE id = %s", (id,))
        data = cursor.fetchone()
        task = {"id": data[0], "name": data[1], "status": data[2]}
        cursor.close()
        return task

    def deleteTask(self, id):
        cursor = self.__conn.cursor()
        sql = "DELETE FROM tasks WHERE id = %s;"
        cursor.execute(sql, (id,))
        self.__conn.commit()
        cursor.close()
