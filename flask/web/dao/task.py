from mysql.connector import Error
from web.domain.task import Task, TaskStatus


class MySQLTaskDAO():
    __conn = None

    def __init__(self, conn):
        self.__conn = conn

    def get(self, id: int):
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT id, name, status FROM tasks WHERE id = %s", (id,))
        data = cursor.fetchone()
        if data is None:
            return None
        task = Task(id=data[0], name=data[1], status=TaskStatus(data[2]))
        cursor.close()
        return task

    def get_tasks(self):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, name, status FROM tasks;")
        tasks = []
        for (id, name, status) in cursor:
            tasks.append(Task(id=id, name=name, status=TaskStatus(status)))
        cursor.close()
        return tasks

    def add_task(self, name, status: TaskStatus):
        cursor = self.__conn.cursor()
        sql = "INSERT INTO tasks (name, status) VALUES (%s, %s)"
        cursor.execute(sql, (name, status.value))
        self.__conn.commit()
        id = cursor.lastrowid
        cursor.close()
        return self.get(id)

    def update_task(self, id: int, name: str, status: TaskStatus):
        cursor = self.__conn.cursor()
        sql = "UPDATE tasks SET name = %s, status = %s WHERE id = %s;"
        cursor.execute(sql, (name, status.value, id))
        self.__conn.commit()
        cursor.close()
        return self.get(id)

    def delete_task(self, id):
        cursor = self.__conn.cursor()
        sql = "DELETE FROM tasks WHERE id = %s;"
        cursor.execute(sql, (id,))
        self.__conn.commit()
        cursor.close()
