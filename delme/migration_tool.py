from sqlite_adapter import SqliteDatabaseAdapter

#ctrl-a :  set-option repeat-time 0

file_handle = open("example_migration.migration","r")

dAdapter = SqliteDatabaseAdapter.getInstance()

file_contents = file_handle.readlines()
i = 0
while i < len(file_contents):
    current_command = file_contents[i].split(" ")[0]
    if current_command == "add":
        acting_on = file_contents[i].split(" ")[1]
        if acting_on == "table":
            table = file_contents[i].split(" ")[2]
            if dAdapter.doesTableExist(table):
                pass
            else:
                dAdapter.createTable(table)
        elif acting_on == "column":
            table = file_contents[i].split(" ")[2]
            column = file_contents[i].split(" ")[3]
            if dAdapter.doesTableExist(table):
                if not dAdapter.doesColumnExist(table, column):
                    dAdapter.addColumn(table,column)
    elif current_command == "remove":
        acting_on = file_contents[i].split(" ")[1]
        if acting_on == "table":
            table = file_contents[i].split(" ")[2].strip()
            if dAdapter.doesTableExist(table):
                dAdapter.dropTable(table)
        elif acting_on == "column":
            table = file_contents[i].split(" ")[2].strip()
            column = file_contents[i].split(" ")[3].strip()
            if dAdapter.doesTableExist(table) and dAdapter.doesColumnExist(table,column):
                dAdapter.deleteColumnFromTable(table,column)
    else:
        pass

    i = i + 1
