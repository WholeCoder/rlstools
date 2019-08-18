from sqlite_adapter import SqliteDatabaseAdapter


class BaseRlsRecord(dict):

    def __init__(self, d):
        super(BaseRlsRecord, self).__init__(d)
        self.dAdapter = SqliteDatabaseAdapter.getInstance()
        print("getting instance in base rls record."+SqliteDatabaseAdapter.getInstance().db_filename)# noqa

    def getOneToManyDictionary(self):
        pass

    def getOneToOneDictionary(self):
        pass

    def __getattr__(self, attr):

        print("tableName == "+str(attr.split("_")))
        tableName = attr.split("_")[2].strip()
        
        if attr.split("_")[1] == "all":
            one_to_many_dictionary = self.getOneToManyDictionary()

            cls = one_to_many_dictionary[tableName][0]
            rs = SqliteDatabaseAdapter.getInstance().findAllRecordsByKey(tableName.strip(),one_to_many_dictionary[tableName][1], self['primary_key'])  # noqa
            rowWithWrapper = [cls(d) for d in rs]
            def wrapper():
                return rowWithWrapper
            return wrapper
        elif attr.split("_")[1] == "one":
            one_to_one_dictionary = self.getOneToOneDictionary()

            cls = one_to_one_dictionary[tableName][0]
            rs = SqliteDatabaseAdapter.getInstance().findAllRecordsByKey(tableName.strip().strip(),"primary_key", self[one_to_one_dictionary[tableName][1]]) # noqa
            if len(rs) == 1:
                def wrapper():
                    return cls(rs[0])
                return wrapper
            elif len(rs) == 0:
                def wrapper():
                    return cls({})
                return wrapper
            else:
                raise Exception("Duplicates in one to many - " + tableName + "[ " + one_to_many_dictionary[tableName][1]+" ]")  # noqa

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
