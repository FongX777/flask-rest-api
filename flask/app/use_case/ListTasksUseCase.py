class ListTasksUseCase:
    __taskDAO = None

    def __init__(self, taskDAO):
        self.__taskDAO = taskDAO

    def execute(self):
        result = self.__taskDAO.getTasks()
        print(result)
        return {"result": result}
