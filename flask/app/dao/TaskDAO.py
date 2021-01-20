class TaskDAO(object):
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
