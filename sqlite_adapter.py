class DatabaseAdapter:
    def __init__(self):
        self.conn = sqlite3.connect('my_test_db.db')
        print("Sqlite adapter - Initializing adapter")

    def doesColumnExist(self,table, column):i
        print("SqliteAdapter - Seeing if column " + column + " exists on table " + table)
        cur = self.conn.cursor()
        columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]
        column = column.split(":")[0].strip()
    
        print("doesColumnExist(conn,"+table+","+column+")")
        if column in columns: 
            print("\tColumn "+column+" in table " + table + " does not exist")
            print("column returned " + str(column not in columns))
            return True
        else:
            print("\tColumn " + column + " already exists on table " + table)
            print("column returned " + str(column not in columns))
            return False
   

    def deleteColumnFromTable(self,table, column):
        print("i--------------------------inside deleteColumnFromTable function")
	    if doesColoumnExist(table,column): 
		cur = self.conn.cursor()
		tablebakdrp = "CREATE TABLE t1_backup (primary_key INTEGER PRIMARY KEY )"
		cur.execute(tablebakdrp)
		dropBackupTableStatement = "drop table t1_backup"
		cur.execute(dropBackupTableStatement)

		columns = [i[1] for i in cur.execute('PRAGMA table_info('+table+')')]

		selectClause = " "
		for columnInColumns in columns:
		    if columnInColumns != column:
		        selectClause = columnInColumns + ","
		selectClause = selectClause[:len(selectClause)-1]
		selectStatement ="CREATE TABLE t1_backup AS SELECT "+selectClause+" FROM "+table  
		print("\n\t"+selectStatement)
		cur.execute(selectStatement)
		# CREATE TABLE t1_backup AS SELECT a, b FROM t1;
		dropTableStatement = "drop table "+table
		print("\n\t" + dropTableStatement)
		cur.execute(dropTableStatement)
		# DROP TABLE t1;
		alterTableStatement = "ALTER TABLE t1_backup RENAME TO " + table
		print("\n\t"+ alterTableStatement)
		cur.execute(alterTableStatement) 
		# ALTER TABLE t1_backup RENAME TO t1;

	#"   SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+table+"'"

        

    def doesTableExist(self,table):
        print("SqliteAdapter - Seeing if table "+ table +" exists.")
        checkIfTableExists = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+table+"'"
        c = self.conn.cursor()               
        print("check if table exists string    "+checkIfTableExists)
        c.execute(checkIfTableExists)
                    
        #if the count is 1, then table exists
        if c.fetchone()[0]==1: 
            print('Table alreaday exists!')
            return True
        else:
            return False                 



    def createTable(self,table):
        c = self.conn.cursor()
        createTableString = "CREATE TABLE "+file_contents[i].split(" ")[2]+" (primary_key INTEGER PRIMARY KEY )"
        c.execute(createTableString)
        print("DatabaseAdapter - Creating table "+table)

    def addColumn(self,table, column):
        print("DatabaseAdapter - Added column "+column+" to table "+ table)

    def removeTable(self,table):
        print("DatabaseAdapter - Removing table "+ table)

    def dropTable(table):
        dropTableStatement = "drop table "+table
        print("\n\t" + dropTableStatement)
        cur.execute(dropTableStatement)


