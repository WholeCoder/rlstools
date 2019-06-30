from database_adapter import DatabaseAdapter
from sqlite_adapter import CursorByName
from sqlite_adapter import SqliteDatabaseAdapter

class BaseRlsRecord:
    def __init__(self):
        self.dAdapter = SqliteDatabaseAdapter.getInstance()
        print("getting instance in base rls record."+SqliteDatabaseAdapter.getInstance().db_filename)

    def typename(self,x):
        return type(x).__name__

    def get_type_name_of_subclass(self):
        return self.typename(self)

    def create(self,insertDictionary):
        table = self.get_type_name_of_subclass()
        self.dAdapter.createNewRecord(table,insertDictionary)

    def findAll(self):
        rows = self.dAdapter.findAllRecords(self.get_type_name_of_subclass())
       
        #for row in rows:
        #    print("rows2 == "+str(row))

        return rows 
