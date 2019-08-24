import sqlite3
from database_adapter import DatabaseAdapter
import yaml
from table_not_found_error import TableNotFoundError
from sqlite3 import OperationalError
import os
import logging

# refer to server.py to disable/enable logging.
#  logging.disable(logging.DEBUG)


class SqliteDatabaseAdapter(DatabaseAdapter):

    __instance = None

    @staticmethod
    def getInstance():
        with open(os.path.join('.', 'config.yaml')) as f:
            # use safe_load instead load
            dataMap = yaml.safe_load(f)
        db_filename = dataMap['config']['database']
        if SqliteDatabaseAdapter.__instance is None:
            SqliteDatabaseAdapter(db_filename)
        return SqliteDatabaseAdapter.__instance

    @staticmethod
    def getTestInstance():
        db_filename = "./my_test_db.db"
        if SqliteDatabaseAdapter.__instance is None:
            SqliteDatabaseAdapter(db_filename)
        return SqliteDatabaseAdapter.__instance

    def __init__(self, db_filename):
        if SqliteDatabaseAdapter.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SqliteDatabaseAdapter.__instance = self
        self.conn = sqlite3.connect(db_filename)
        self.db_filename = db_filename

    def getColumnTypeDictionary(self, table):
        self.conn = sqlite3.connect(self.db_filename)
        cur = self.conn.cursor()
        columnDictionary = {i[1].strip(): i[2].strip() for i in cur.execute('PRAGMA table_info('+table+')')}  # noqa
        self.conn.commit()
        self.conn.close()
        return columnDictionary

    def doesColumnExist(self, table, column):
        self.conn = sqlite3.connect(self.db_filename)
        cur = self.conn.cursor()
        columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]
        column = column.split(":")[0].strip()
        self.conn.commit()
        if column in columns:
            return True
        else:
            pass
            return False

    def getNextDatabaseVersionNumber(self):
        if not self.doesTableExist("db_versions"):
            self.createTable("db_versions")
            self.addColumn("db_versions", "version", "string")
            return "000"
        elif len(self.findAllRecords("db_versions")) == 0:
            return "000"
        else:
            rows = self.findAllRecords("db_versions")
            lst = []
            for r in rows:
                lst.append(r['version'])
            lst.sort(reverse=True)
            max = int(lst[0])
            new_max = max + 1
            if new_max < 10:
                nn = "00" + str(new_max)
            elif new_max < 100:
                nn = "00" + str(new_max)
            return nn

    def deleteColumnFromTable(self, table, column):
        if not self.doesTableExist(table):
            return
        else:
            pass

        if self.doesColumnExist(table, column):
            self.cur = self.conn.cursor()
            if self.doesTableExist("t1_backup"):
                self.dropTable("t1_backup")

            columns = [i[1] for i in self.cur.execute('PRAGMA table_info(' + table + ')')]# noqa
            selectClause = " "
            for columnInColumns in columns:
                if columnInColumns.strip() != column.strip():
                    selectClause = selectClause + columnInColumns + ","
            selectClause = selectClause[:len(selectClause)-1]
            selectStatement = "CREATE TABLE t1_backup AS SELECT " + selectClause + " FROM "+table# noqa
            self.cur.execute(selectStatement)
            dropTableStatement = "drop table "+table
            self.cur.execute(dropTableStatement)
            alterTableStatement = "ALTER TABLE t1_backup RENAME TO " + table
            self.cur.execute(alterTableStatement)
            self.conn.commit()

    def doesTableExist(self, table):
        checkIfTableExists = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+table+"'" # noqa
        self.conn = sqlite3.connect(self.db_filename)
        c = self.conn.cursor()
        c.execute(checkIfTableExists)

        # if the count is 1, then table exists
        foundOne = (c.fetchone()[0] == 1)
        self.conn.commit()

        if foundOne:
            return True
        else:
            return False

    def createTable(self, table):
        self.conn = SqliteDatabaseAdapter.getInstance().conn = sqlite3.connect(self.db_filename)# noqa
        self.c = SqliteDatabaseAdapter.getInstance().conn.cursor()
        table = table.strip()
        if self.doesTableExist(table):
            return
        createTableString = "CREATE TABLE "+table+" (primary_key INTEGER PRIMARY KEY )" # noqa
        self.c.execute(createTableString)
        self.conn.commit()

    def addColumn(self, table, column, tpe):
        self.conn = sqlite3.connect(self.db_filename)
        self.c = self.conn.cursor()

        if tpe.strip() == "string":
            add_type = "TEXT"
        elif tpe.strip() == "integer":
            add_type = "INTEGER"
        elif tpe.strip() == "float":
            add_type = "REAL"

        if self.doesColumnExist(table, column):
            return
        logging.info("add_type == " + add_type)
        dbQuery = 'ALTER TABLE '+table+' ADD COLUMN '+column.split(":")[0]+' '+add_type # noqa
        self.c.execute(dbQuery)

        self.conn.commit()
        self.conn.close()

    def removeTable(self, table):
        self.conn = sqlite3.connect(self.db_filename)
        self.dropTable(self, table)
        self.conn.commit()
        self.conn.close()
        # print("DatabaseAdapter - Removing table "+ table)

    def dropTable(self, table):
        self.conn = sqlite3.connect(self.db_filename)
        table = table.strip()
        cur = self.conn.cursor()
        dropTableStatement = "drop table "+table
        cur.execute(dropTableStatement)
        self.conn.commit()
        self.conn.close()

    def deleteRowFromTable(self, table, key, value):
        self.conn = sqlite3.connect(self.db_filename)
        cur = self.conn.cursor()
        deleteStatement = "DELETE FROM " + table + " WHERE "+key+"='"+str(value)+"'" # noqa
        cur.execute(deleteStatement)
        self.conn.commit()
        cur.close()

    def createNewRecord(self, table, insertDictionary):
        if len(insertDictionary.keys()) == 0:
            return

        typeDictionary = self.getColumnTypeDictionary(table)

        self.conn = sqlite3.connect(self.db_filename)
        cur = self.conn.cursor()

        insertString = ""
        valueString = ""
        for col in insertDictionary.keys():
            if typeDictionary[col].strip() == 'TEXT':
                insertString += col+","
                valueString += "'"+insertDictionary[col]+"',"
            elif typeDictionary[col].strip() == 'INTEGER' or typeDictionary[col].strip() == 'REAL':  # noqa
                insertString += col+","
                valueString += insertDictionary[col].strip()+","

        insertString = insertString[:-1]
        valueString = valueString[:-1]

        finalString = "INSERT INTO " + table + "("+insertString+") VALUES (" + valueString + ")"# noqa

        logging.info("insert string == " + finalString)
        cur.execute(finalString)
        self.conn.commit()
        self.conn.close()

    def findAllRecords(self, table):
        self.conn = sqlite3.connect(self.db_filename)
        cur = self.conn.cursor()
        columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]
        colString = ""
        for col in columns:
            colString += col+","

        colString = colString[:-1]
        logging.info("---------------------------------> table = " + table)
        selectStatement = "SELECT " + colString + " FROM "+table
        logging.info(" SQL STATEMENT = " + selectStatement)
        curr = self.conn.cursor()
        logging.info('...............test')
        try:
            curr.execute(selectStatement)
        except OperationalError as err:
            raise TableNotFoundError("Table " + table + " not found! - Be sure to run migration_tool upgrade!!!")  # noqa
            #  raise err
        data = []
        for row in CursorByName(curr):
            data.append(row)
        self.conn.commit()
        self.conn.close()
        return data

    def findAllRecordsByKey(self, table, key, value):
        self.conn = sqlite3.connect(self.db_filename)
        cur = self.conn.cursor()
        columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]
        colString = ""
        for col in columns:
            colString += col+","

        colString = colString[:-1]
        logging.info("---------------------------------> table = " + table)
        selectStatement = "SELECT " + colString + " FROM "+table + " WHERE " + key + " = " + str(value) + ""  # noqa
        logging.info(" SQL STATEMENT = " + selectStatement)
        curr = self.conn.cursor()
        logging.info('...............test')
        try:
            curr.execute(selectStatement)
        except OperationalError as err:
            raise TableNotFoundError("Table " + table + " not found! - Be sure to run migration_tool upgrade!!!")  # noqa
            #  raise err
        data = []
        for row in CursorByName(curr):
            data.append(row)
        self.conn.commit()
        self.conn.close()
        return data


class CursorByName():
    def __init__(self, cursor):
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        row = self._cursor.__next__()

        return {description[0]: row[col] for col, description in enumerate(self._cursor.description) }# noqa
