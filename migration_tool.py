import os
import sys
from sqlite_adapter import SqliteDatabaseAdapter

#ctrl-a :  set-option repeat-time 0
dAdapter = SqliteDatabaseAdapter.getInstance()

shouldUpgrade = sys.argv[1] == "upgrade"

next_available_database_version = dAdapter.getNextDatabaseVersionNumber()

files = os.listdir(".")
num_list = []

if shouldUpgrade:
    for f in files:
        part = f.split("_")[0]
        if part >= next_available_database_version:
            num_list.append(part)
else:
    # Delete all the tables if downgrading
    for f in files:
        part = f.split("_")[0]
        num_list.append(part)

num_list.sort()

for f in num_list:
    file_handle = open(f+"_migration","r")
    

    file_contents = file_handle.readlines()
    i = 0
    while i < len(file_contents):
        current_command = file_contents[i].split(" ")[0]
        if current_command == "add" and shouldUpgrade:
            acting_on = file_contents[i].split(" ")[1]
            if acting_on == "table":
                dAdapter.createNewRecord("db_versions",{"version":f})
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
        elif current_command == "remove" and not shouldUpgrade:
            acting_on = file_contents[i].split(" ")[1]
            if acting_on == "table":
                dAdapter.deleteRowFromTable("db_versions","version",f)
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
