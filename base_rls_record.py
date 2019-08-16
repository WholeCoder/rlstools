from sqlite_adapter import SqliteDatabaseAdapter


class BaseRlsRecord(dict):
    def __init__(self, d):
        super(BaseRlsRecord, self).__init__(d) 
        self.dAdapter = SqliteDatabaseAdapter.getInstance()
        print("getting instance in base rls record."+SqliteDatabaseAdapter.getInstance().db_filename)# noqa

    def typename(self, x):
        return type(x).__name__

    def get_type_name_of_subclass(self):
        return self.typename(self)

    def create(self, insertDictionary):
        table = self.get_type_name_of_subclass()
        self.dAdapter.createNewRecord(table, insertDictionary)

    @classmethod
    def findAll(cls):
        rows = SqliteDatabaseAdapter.getInstance().findAllRecords(cls.__name__)
        rowWithWrapper = [cls(d) for d in rows]
        return rowWithWrapper
