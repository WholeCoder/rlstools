class DatabaseAdapter:
    def __init__(self):
        print("DatabaseAdapter - Initializing adapter")

    def doesColumnExist(self, table, column):
        print("DatabaseAdapter - Seeing if column " + column + " exists on table " + table)# noqa

    def deleteColumnFromTable(self, table, column):
        print("DatabaseAdapter - Deleting column " + column + " from table "+table)# noqa

    def doesTableExist(self, table):
        print("DatabaseAdapter - Seeing if table " + table + " exists.")

    def createTable(self, table):
        print("DatabaseAdapter - Creating table "+table)

    def addColumn(self, table, column):
        print("DatabaseAdapter - Added column "+column+" to table " + table)

    def removeTable(self, table):
        print("DatabaseAdapter - Removing table " + table)

    def dropTable(self, table):
        print("DatabaseAdapter - Dropping table " + table)


