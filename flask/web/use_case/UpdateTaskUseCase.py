class UpdateTaskUseCase:
    __taskDAO = None

    def __init__(self, taskDAO):
        self.__taskDAO = taskDAO

    def execute(self, id, name, status):
        result = self.__taskDAO.updateTask(id, name, status)
        return result
