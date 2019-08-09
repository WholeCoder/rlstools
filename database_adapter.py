from abc import ABCMeta, abstractmethod


class DatabaseAdapter(metaclass=ABCMeta):
    def __init__(self):
        print("DatabaseAdapter - Initializing adapter")

    @abstractmethod
    def doesColumnExist(self, table, column):
        pass

    @abstractmethod
    def deleteColumnFromTable(self, table, column):
        pass

    @abstractmethod
    def doesTableExist(self, table):
        pass

    @abstractmethod
    def createTable(self, table):
        pass

    @abstractmethod
    def addColumn(self, table, column):
        pass

    @abstractmethod
    def removeTable(self, table):
        pass

    @abstractmethod
    def dropTable(self, table):
        pass
