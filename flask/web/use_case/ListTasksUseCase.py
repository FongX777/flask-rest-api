class ListTasksUseCase:
    __taskDAO = None

    def __init__(self, taskDAO):
        self.__taskDAO = taskDAO

    def execute(self):
        result = self.__taskDAO.getTasks()
        return {"result": result}
