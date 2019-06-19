from sqlite_adapter import SqliteDatabaseAdapter

#ctrl-a :  set-option repeat-time 0

file_handle = open("example_migration.migration","r")

dAdapter = SqliteDatabaseAdapter("my_db.db")

file_contents = file_handle.readlines()
i = 0
while i < len(file_contents):
    current_command = file_contents[i].split(" ")[0]
    if current_command == "add":
        print("add")
        acting_on = file_contents[i].split(" ")[1]
        if acting_on == "table":
            table = file_contents[i].split(" ")[2]
            print("---------------------------"+table+"---------exists!")
            if dAdapter.doesTableExist(table):
                print("      table exists here")
                pass
            else:
                print("table doesn't exist here")
                dAdapter.createTable(table)
            print("\ttable")
        elif acting_on == "column":
            table = file_contents[i].split(" ")[2]
            column = file_contents[i].split(" ")[3]
            if dAdapter.doesTableExist(table):
                if not dAdapter.doesColumnExist(table, column):
                    dAdapter.addColumn(table,column)
            print("\tcolumn")
    elif current_command == "remove":
        print("remove")
        acting_on = file_contents[i].split(" ")[1]
        if acting_on == "table":
            table = file_contents[i].split(" ")[2].strip()
            if dAdapter.doesTableExist(table):
                print("dropping table in migration tool 2: "+table)
                dAdapter.dropTable(table)
            print("\ttable")
        elif acting_on == "column":
            table = file_contents[i].split(" ")[2].strip()
            column = file_contents[i].split(" ")[3].strip()
            if dAdapter.doesTableExist(table) and dAdapter.doesColumnExist(table,column):
                print("deleteing column "+column+" from table "+table)
                dAdapter.deleteColumnFromTable(table,column)
            print("\tcolumn")
    else:
        pass

    i = i + 1