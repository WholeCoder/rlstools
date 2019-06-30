import sqlite3
import atexit
from database_adapter import DatabaseAdapter

class SqliteDatabaseAdapter(DatabaseAdapter):

    __instance = None

    @staticmethod
    def getInstance():
        db_filename="./my_db.db"
        if SqliteDatabaseAdapter.__instance == None:
            SqliteDatabaseAdapter(db_filename)
        return SqliteDatabaseAdapter.__instance

    @staticmethod
    def getTestInstance():
        print("SqliteDataseAdapter.__instance == " + str(SqliteDatabaseAdapter.__instance))
        db_filename = "./my_test_db.db"
        if SqliteDatabaseAdapter.__instance == None:
            SqliteDatabaseAdapter(db_filename)
        return SqliteDatabaseAdapter.__instance

    def __init__(self,db_filename):
        if SqliteDatabaseAdapter.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SqliteDatabaseAdapter.__instance = self
        print("------------> attaching connection")
        self.conn = sqlite3.connect(db_filename)
        self.db_filename = db_filename
        # print("Sqlite adapter - Initializing adapter")
        # atexit.register(self.cleanup)

    # def cleanup(self):
    #     # print("Running cleanup...")
    #     self.conn.close()

    def doesColumnExist(self,table, column):
        # print("SqliteAdapter - Seeing if column " + column + " exists on table " + table)
        self.conn = sqlite3.connect(self.db_filename)
        cur = self.conn.cursor()
        columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]
        column = column.split(":")[0].strip()
        #print("-----------------------column without :::: == "+column)
        # print("doesColumnExist(conn,"+table+","+column+")")
        self.conn.commit()
        if column in columns:
            #print("\tColumn "+column+" in table " + table + " does not exist")
            # print("column returned " + str(column not in columns))
            return True
        else:
            pass
            #print("\tColumn " + column + " already exists on table " + table)
            # print("column returned " + str(column not in columns))
            return False


    def deleteColumnFromTable(self,table, column):
        # print("i--------------------------inside deleteColumnFromTable function")
        if not self.doesTableExist(table):
            #print("1. table does not exist. " + table)
            return
        else:
            #print("1. table does "+table+" exists.")
            pass

        if self.doesColumnExist(table,column):
            self.cur = self.conn.cursor()
            if self.doesTableExist("t1_backup"):
                self.dropTable("t1_backup")
                #print("2.  droppng table t1_backup")
            #tablebakdrp = "CREATE TABLE t1_backup (primary_key INTEGER PRIMARY KEY )"
            #self.cur.execute(tablebakdrp)
            #dropBackupTableStatement = "drop table t1_backup"
            #self.cur.execute(dropBackupTableStatement)

            columns = [i[1] for i in self.cur.execute('PRAGMA table_info('+table+')')]
            #print("columns == " + ",".join(columns))
            selectClause = " "
            for columnInColumns in columns:
                if columnInColumns.strip() != column.strip():
                    selectClause = selectClause + columnInColumns + ","
            selectClause = selectClause[:len(selectClause)-1]
            #print("selectClause == " + selectClause)
            selectStatement ="CREATE TABLE t1_backup AS SELECT "+selectClause+" FROM "+table
            #print("selectStatement:  "+selectStatement)
           ##rint("select Statement for create backup table:  "+selectStatement)
            # print("\n\t"+selectStatement)
            self.cur.execute(selectStatement)
            # CREATE TABLE t1_backup AS SELECT a, b FROM t1;
            dropTableStatement = "drop table "+table
            #print("4. dropping table "+table)
            # print("\n\t" + dropTableStatement)
            self.cur.execute(dropTableStatement)
		# DROP TABLE t1;
            alterTableStatement = "ALTER TABLE t1_backup RENAME TO " + table
            # print("\n\t"+ alterTableStatement)
            #print("renaming t1_backup to "+table)
            self.cur.execute(alterTableStatement)
	    # ALTER TABLE t1_backup RENAME TO t1;
            self.conn.commit()
	#"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+table+"'"



    def doesTableExist(self,table):
        # print("SqliteAdapter - Seeing if table "+ table +" exists.")
        checkIfTableExists = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+table+"'"
        self.conn = sqlite3.connect(self.db_filename)
        c = self.conn.cursor()
        # print("check if table exists string    "+checkIfTableExists)
        c.execute(checkIfTableExists)

        #if the count is 1, then table exists
        foundOne = (c.fetchone()[0]==1)
        self.conn.commit()

        if foundOne:
            # print('Table alreaday exists!')
            #print("table exists in adapter.")
            return True
        else:
            #print("Table doesen't exist in adapter")
            return False



    def createTable(self,table):
        self.conn = SqliteDatabaseAdapter.getInstance().conn = sqlite3.connect(self.db_filename)
        self.c = SqliteDatabaseAdapter.getInstance().conn.cursor()
        table = table.strip()
        #print("self.doesTableExist("+table+") == "+str(self.doesTableExist(table)))
        if self.doesTableExist(table):
            return
        #print("--creating table")
        createTableString = "CREATE TABLE "+table+" (primary_key INTEGER PRIMARY KEY )"
        self.c.execute(createTableString)
        # print("DatabaseAdapter - Creating table "+table)
        self.conn.commit()


    def addColumn(self,table, column):
        self.conn = sqlite3.connect(self.db_filename)
        self.c = self.conn.cursor()

        if self.doesColumnExist(table, column):
            return
        dbQuery = 'ALTER TABLE '+table+' ADD COLUMN '+column.split(":")[0]+' TEXT'
        print("dbQuery == " + dbQuery)
        self.c.execute(dbQuery)

        print("SqliteDatabaseAdapter - Added column "+column+" to table "+ table)
        self.conn.commit()
        self.conn.close()

    def removeTable(self,table):
        self.conn = sqlite3.connect(self.db_filename)
        self.dropTable(self,table)
        self.conn.commit()
        self.conn.close()
        # print("DatabaseAdapter - Removing table "+ table)

    def dropTable(self,table):
        self.conn = sqlite3.connect(self.db_filename)
        #print("dropping table "+table)
        table = table.strip()
        cur = self.conn.cursor()
        dropTableStatement = "drop table "+table
        #print("\n\t3. " + dropTableStatement)
        cur.execute(dropTableStatement)
        self.conn.commit()
        self.conn.close()

    def createNewRecord(self,table,insertDictionary):
        self.conn = sqlite3.connect(self.db_filename)
        cur = self.conn.cursor()
        columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]

        insertString = ""
        valueString = ""
        for col in insertDictionary.keys():
            if col != "primary_key":
                insertString += col+","
                valueString += "'"+insertDictionary[col]+"',"

        insertString = insertString[:-1]
        valueString = valueString[:-1]

        finalString = "INSERT INTO "+table+ "("+insertString+") VALUES ("+valueString+")"
        print("finalString == "+finalString)
        cur.execute(finalString)
        self.conn.commit()
        self.conn.close()

    def findAllRecords(self,table):
        self.conn = sqlite3.connect(self.db_filename)
        cur = self.conn.cursor()

        columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]

        colString = ""
        for col in columns:
            colString += col+","

        colString = colString[:-1]
        selectStatement = "SELECT " + colString + " FROM "+table

        curr = self.conn.cursor()
        curr.execute(selectStatement)

        data = []
        for row in CursorByName(curr):
           #print("row1 == "+str(row))
           data.append(row)
        self.conn.commit()
        self.conn.close()
        return data #CursorByName(curr)


class CursorByName():
    def __init__(self, cursor):
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        row = self._cursor.__next__()

        return { description[0]: row[col] for col, description in enumerate(self._cursor.description) }

#for row in CursorByName(cur):
#    print(row)

print(SqliteDatabaseAdapter.getTestInstance())
SqliteDatabaseAdapter.getTestInstance().createTable("Person")
