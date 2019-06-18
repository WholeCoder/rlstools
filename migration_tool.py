from sqlite_adapter import SqliteDatabaseAdapter

#ctrl-a :  set-option repeat-time 0

file_handle = open("example_migration.migration","r")

dAdapter = SqliteDatabaseAdapter("my_db.db")

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
                command_acting_on = file_contents[i].split(" ")[1]

                if command_acting_on == "table":
                    table = file_contents[i].split(" ")[2].strip()
                    print("adding table "+table)
    
                    if dAdapter.doesTableExist(table):
                        print("Table "+table + " already exists.")
                    else:
                        dAdapter.createTable( table  )
                        print("Table "+table+" is being created.")
                elif command_acting_on == "column":

                    tableName = file_contents[i].split(" ")[2].strip()
                    if dAdapter.doesTableExist(tableName):
                    #print("\tadding column "+file_contents[i].split(" ")[3].strip())
                        column_name = file_contents[i].split(" ")[3].strip()
                        if not dAdapter.doesColumnExist(tableName,column_name):
                            dAdapter.addColumn( tableName, column_name)
                i = i+1
        
        split_line = file_contents[i].split(' ')
        if split_line[0].strip() == "downgrade":
            print(split_line[0].strip())
            i = i+1
            while i in range(len(file_contents)) and file_contents[i].strip() != "" and file_contents[i] != '':
                if file_contents[i].strip().startswith("#"):
                    i = i + 1
                    continue
                command = file_contents[i].split(" ")[1]
                if command == "table":
                    print("----------- does table Exist:  " + str(dAdapter.doesTableExist(file_contents[i].split(" ")[2].strip())))
                    print("          value: " + file_contents[i].split(" ")[2])
                    tableName = file_contents[i].split(" ")[2].strip()
                    if dAdapter.doesTableExist(tableName):

                        print("removing table "+tableName)
                        # deleteColumnFromTable(conn, file_contents[i].split(" ")[2].strip(),file_contents[i].split(" ")[3].strip()) 
                        dAdapter.dropTable( tableName)
                elif command == "column":
                    tableName = file_contents[i].split(" ")[2]
                    column_name = file_contents[i].split(" ")[3]
                    print(" checking to removed == "+tableName+", "+column_name)
                    #print(doesColoumnExist(file_contents[i].split(" ")[2].strip(),file_contents[i].split(" ")[3].strip()))
                    if dAdapter.doesTableExist(tableName.strip()) and dAdapter.doesColumnExist(tableName.strip(),column_name.strip()):
                       
                        dAdapter.deleteColumnFromTable(tableName,column_name.strip())
                        
                        print("\tremoving column "+column_name.strip())
                i = i+1
    i = i + 1

