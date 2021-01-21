class DeleteTaskUseCase:
    __taskDAO = None

    def __init__(self, taskDAO):
        self.__taskDAO = taskDAO

    def execute(self, id):
        self.__taskDAO.deleteTask(id)
