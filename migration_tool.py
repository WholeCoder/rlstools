import sqlite3
#ctrl-a :  set-option repeat-time 0

conn = sqlite3.connect('my_db.db')

file_handle = open("example_migration.migration","r")


def doesColoumnExist(conn,table,column):
    cur = conn.cursor()
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

def deleteColumnFromTable(conn, table, column):
    print("i--------------------------inside deleteColumnFromTable function")
    if doesColoumnExist(conn,table,column): 
        cur = conn.cursor()
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


def doesTableExist(conn,table):
    checkIfTableExists = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+file_contents[i].split(" ")[2].strip()+"'"
    c = conn.cursor()               
    print("check if table exists string    "+checkIfTableExists)
    c.execute(checkIfTableExists)
                    
    #if the count is 1, then table exists
    if c.fetchone()[0]==1: 
        print('Table alreaday exists!')
        return True
    else:
        return False                 

file_contents = file_handle.readlines()
for i in range(len(file_contents)):
    if file_contents[i].strip() != '\n':
        split_line = file_contents[i].split(' ')
        if split_line[0].strip().startswith("#"):
            i = i + 1
            continue
        if split_line[0].strip() == "upgrade":
            print(split_line[0].strip())
            i = i+1
            while i in range(len(file_contents)) and file_contents[i].strip() != "" and file_contents[i] != 'downgrade':
                if file_contents[i].strip().startswith("#"):
                    i = i + 1
                    continue
                if file_contents[i].split(" ")[1] == "table":
                    print("adding table "+file_contents[i].split(" ")[2].strip())
                    c = conn.cursor()
    
                    if doesTableExist(conn,file_contents[i].split(" ")[2].strip()):
                        print("Table "+file_contents[i].split(" ")[2].strip() + " already exists.")
                    else:
                        createTableString = "CREATE TABLE "+file_contents[i].split(" ")[2]+" (primary_key INTEGER PRIMARY KEY )"
                        c.execute(createTableString)
                elif file_contents[i].split(" ")[1] == "column":
                    if doesTableExist(conn,file_contents[i].split(" ")[2].strip()):
                    #print("\tadding column "+file_contents[i].split(" ")[3].strip())

                        if not doesColoumnExist(conn,file_contents[i].split(" ")[2],file_contents[i].split(" ")[3].strip()):
                            c = conn.cursor()
                            c.execute('ALTER TABLE '+file_contents[i].split(" ")[2]+' ADD COLUMN '+file_contents[i].split(" ")[3].split(':')[0]+' TEXT')
                i = i+1
        
        split_line = file_contents[i].split(' ')
        if split_line[0].strip() == "downgrade":
            print(split_line[0].strip())
            i = i+1
            while i in range(len(file_contents)) and file_contents[i].strip() != "" and file_contents[i] != '':
                if file_contents[i].strip().startswith("#"):
                    i = i + 1
                    continue
                if file_contents[i].split(" ")[1] == "table":
                    if doesTableExist(conn,file_contents[i].split(" ")[2]):

                        print("removing table "+file_contents[i].split(" ")[2].strip())
                        # deleteColumnFromTable(conn, file_contents[i].split(" ")[2].strip(),file_contents[i].split(" ")[3].strip()) 
                        c = conn.cursor()
                        c.execute("DROP TABLE "+file_contents[i].split(" ")[2])
                elif file_contents[i].split(" ")[1] == "column":
                    print(" checking to removed == "+file_contents[i].split(" ")[2]+", "+file_contents[i].split(" ")[3].strip())
                    print(doesColoumnExist(conn,file_contents[i].split(" ")[2].strip(),file_contents[i].split(" ")[3].strip()))
                    if doesColoumnExist(conn,file_contents[i].split(" ")[2].strip(),file_contents[i].split(" ")[3].strip()):
                       
                        deleteColumnFromTable(conn, file_contents[i].split(" ")[2],file_contents[i].split(" ")[3].strip())
                        
                        print("\tremoving column "+file_contents[i].split(" ")[3].strip())
                i = i+1
    i = i + 1
conn.commit()

