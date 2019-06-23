from database_adapter import DatabaseAdapter

class BaseRlsRecord:
    def __init__(self,dAdapter):
        self.dAdapter = dAdapter

    def typename(self,x):
        return type(x).__name__

    def get_type_name_of_subclass(self):
        return self.typename(self)

    def create(self,insertDictionary):
        table = self.get_type_name_of_subclass()
        self.dAdapter.createNewRecord(table,insertDictionary)

    def findAll(self):
        row = self.dAdapter.findAllRecords(get_type_name_of_subclass())
        
#        for row in CursoerByName(cur):
#            print(row)

        return rows 
