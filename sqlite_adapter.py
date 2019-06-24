import sqlite3
import atexit
from database_adapter import DatabaseAdapter

class SqliteDatabaseAdapter(DatabaseAdapter):
    def __init__(self,db_filename):
        self.conn = sqlite3.connect(db_filename)
        # print("Sqlite adapter - Initializing adapter")
        atexit.register(self.cleanup)

    def cleanup(self):
        # print("Running cleanup...")
        self.conn.close()

    def doesColumnExist(self,table, column):
        # print("SqliteAdapter - Seeing if column " + column + " exists on table " + table)
        cur = self.conn.cursor()
        columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]
        column = column.split(":")[0].strip()
        #print("-----------------------column without :::: == "+column)
        # print("doesColumnExist(conn,"+table+","+column+")")
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
        c = self.conn.cursor()               
        # print("check if table exists string    "+checkIfTableExists)
        c.execute(checkIfTableExists)
                    
        #if the count is 1, then table exists
        if c.fetchone()[0]==1: 
            # print('Table alreaday exists!')
            #print("table exists in adapter.")
            return True
        else:
            #print("Table doesen't exist in adapter")
            return False                 



    def createTable(self,table):
        c = self.conn.cursor()
        table = table.strip()
        #print("self.doesTableExist("+table+") == "+str(self.doesTableExist(table)))
        if self.doesTableExist(table):
            return
        #print("--creating table")
        createTableString = "CREATE TABLE "+table+" (primary_key INTEGER PRIMARY KEY )"
        c.execute(createTableString)
        # print("DatabaseAdapter - Creating table "+table)

    def addColumn(self,table, column):
        c = self.conn.cursor()
        c.execute('ALTER TABLE '+table+' ADD COLUMN '+column.split(":")[0]+' TEXT')

        # print("SqliteDatabaseAdapter - Added column "+column+" to table "+ table)

    def removeTable(self,table):
        self.dropTable(self,table)
        # print("DatabaseAdapter - Removing table "+ table)

    def dropTable(self,table):
        #print("dropping table "+table)
        table = table.strip()
        cur = self.conn.cursor()
        dropTableStatement = "drop table "+table
        #print("\n\t3. " + dropTableStatement)
        cur.execute(dropTableStatement)

    def createNewRecord(self,table,insertDictionary):
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
        
    def findAllRecords(self,table):
        cur = self.conn.cursor()

        columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]
        
        colString = ""
        for col in columns:
            colString += col+","

        colString = colString[:-1]
        selectStatement = "SELECT " + colString + " FROM "+table
        
        curr = self.conn.cursor()
        curr.execute(selectStatement)
        
        for row in CursorByName(curr):
            print(row)
        
        return CursorByName(curr)


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


