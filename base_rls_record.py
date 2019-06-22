from database_adapter import DatabaseAdapter

class BaseRlsRecord:
    def __init__(self,dAdapter):
        self.dAdapter = dAdapter

    def typename(self,x):
        return type(x).__name__

    def get_type_name_of_subclass(self):
        return self.typename(self)

    def create(self,table,insertDictionary):
        self.dAdapter.createNewRecord(table,insertDictionary)
