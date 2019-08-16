from sqlite_adapter import SqliteDatabaseAdapter


class BaseRlsRecord(dict):

    def __init__(self, d):
        super(BaseRlsRecord, self).__init__(d)
        self.dAdapter = SqliteDatabaseAdapter.getInstance()
        print("getting instance in base rls record."+SqliteDatabaseAdapter.getInstance().db_filename)# noqa

    def getOneToManyDictionary(self):
        pass

    def __getattr__(self, attr):

        print("tableName == "+str(attr.split("_")))
        tableName = attr.split("_")[2]

        one_to_many_dictionary = self.getOneToManyDictionary()

        cls = one_to_many_dictionary[tableName][0]
        rs = SqliteDatabaseAdapter.getInstance().findAllRecordsByKey(tableName.strip(),one_to_many_dictionary[tableName][1], self['primary_key'])  # noqa
        rowWithWrapper = [cls(d) for d in rs]
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
