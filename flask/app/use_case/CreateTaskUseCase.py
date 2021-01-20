class CreateTaskUseCase:
    __taskDAO = None

    def __init__(self, taskDAO):
        self.__taskDAO = taskDAO

    def execute(self, name):
        result = self.__taskDAO.insertTask(name)
        return result
