from sqlite_adapter import SqliteDatabaseAdapter


class BaseRlsRecord(dict):
    one_to_many_dictionary = {}

    def __init__(self, d):
        super(BaseRlsRecord, self).__init__(d) 
        self.dAdapter = SqliteDatabaseAdapter.getInstance()
        print("getting instance in base rls record."+SqliteDatabaseAdapter.getInstance().db_filename)# noqa

    def __getattr__(self, attr):
        tableName = attr.split("_")[3]
        cls = eval(tableName)
        rows = SqliteDatabaseAdapter.getInstance().findAllRecords(tableName)
        rowWithWrapper = [cls(d) for d in rows]
        return rowWithWrapper

    def typename(self, x):
        return type(x).__name__

    def get_type_name_of_subclass(self):
        return self.typename(self)

    @classmethod
    def create(cls, insertDictionary):
        #  table = self.get_type_name_of_subclass()
        SqliteDatabaseAdapter.getInstance().createNewRecord(cls.__name__, insertDictionary)  # noqa

    @classmethod
    def findAll(cls):
        rows = SqliteDatabaseAdapter.getInstance().findAllRecords(cls.__name__)
        rowWithWrapper = [cls(d) for d in rows]
        return rowWithWrapper
