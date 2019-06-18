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
                if file_contents[i].split(" ")[1] == "table":
                    print("adding table "+file_contents[i].split(" ")[2].strip())
    
                    if dAdapter.doesTableExist(file_contents[i].split(" ")[2].strip()):
                        print("Table "+file_contents[i].split(" ")[2].strip() + " already exists.")
                    else:
                        dAdapter.createTable( file_contents[i].split(" ")[2] )
                elif file_contents[i].split(" ")[1] == "column":
                    if dAdapter.doesTableExist(file_contents[i].split(" ")[2].strip()):
                    #print("\tadding column "+file_contents[i].split(" ")[3].strip())

                        if not dAdapter.doesColumnExist(file_contents[i].split(" ")[2],file_contents[i].split(" ")[3].strip()):
                            dAdapter.addColumn( file_contents[i].split(" ")[2], file_contents[i].split(" ")[3].split(':')[0])
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
                    if dAdapter.doesTableExist(file_contents[i].split(" ")[2]):

                        print("removing table "+file_contents[i].split(" ")[2].strip())
                        # deleteColumnFromTable(conn, file_contents[i].split(" ")[2].strip(),file_contents[i].split(" ")[3].strip()) 
                        dAdapter.dropTable( file_contents[i].split(" ")[2])
                elif file_contents[i].split(" ")[1] == "column":
                    print(" checking to removed == "+file_contents[i].split(" ")[2]+", "+file_contents[i].split(" ")[3].strip())
                    #print(doesColoumnExist(file_contents[i].split(" ")[2].strip(),file_contents[i].split(" ")[3].strip()))
                    if dAdapter.doesColumnExist(file_contents[i].split(" ")[2].strip(),file_contents[i].split(" ")[3].strip()):
                       
                        dAdapter.deleteColumnFromTable(file_contents[i].split(" ")[2],file_contents[i].split(" ")[3].strip())
                        
                        print("\tremoving column "+file_contents[i].split(" ")[3].strip())
                i = i+1
    i = i + 1

