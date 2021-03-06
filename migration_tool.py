#!/usr/bin/python3
import os
import sys
from sqlite_adapter import SqliteDatabaseAdapter

dAdapter = SqliteDatabaseAdapter.getInstance()

shoulddowngrade = sys.argv[1] == "downgrade"
if shoulddowngrade:
    askUserIfTheyReallyWantToDowngrade = input("Are you sure you want to DELETE your ENTIRE DATABASE???   (y,n):  ")# noqa
    if askUserIfTheyReallyWantToDowngrade.lower() != "y":
        sys.exit()

next_available_database_version = dAdapter.getNextDatabaseVersionNumber()

files = os.listdir("./migrations")
num_list = []

if not shoulddowngrade:
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
    with open(os.path.join(os.getcwd(), "migrations",f+"_migration"), "r") as file_handle:  # noqa
        file_contents = file_handle.readlines()
    i = 0
    while i < len(file_contents):
        current_command = file_contents[i].split(" ")[0]
        if current_command == "add" and not shoulddowngrade:
            acting_on = file_contents[i].split(" ")[1]
            if acting_on == "table":
                dAdapter.createNewRecord("db_versions", {"version": f})
                table = file_contents[i].split(" ")[2]
                if dAdapter.doesTableExist(table):
                    pass
                else:
                    dAdapter.createTable(table)
            elif acting_on == "column":
                table = file_contents[i].split(" ")[2]
                column = file_contents[i].split(" ")[3].split(":")[0]
                tpe = file_contents[i].split(" ")[3].split(":")[1]
                if dAdapter.doesTableExist(table):
                    if not dAdapter.doesColumnExist(table, column):
                        dAdapter.addColumn(table, column, tpe)
        elif current_command == "remove" and shoulddowngrade:
            acting_on = file_contents[i].split(" ")[1]
            if acting_on == "table":
                dAdapter.deleteRowFromTable("db_versions", "version", f)
                table = file_contents[i].split(" ")[2].strip()
                if dAdapter.doesTableExist(table):
                    dAdapter.dropTable(table)
            elif acting_on == "column":
                table = file_contents[i].split(" ")[2].strip()
                column = file_contents[i].split(" ")[3].strip()
                if dAdapter.doesTableExist(table) and dAdapter.doesColumnExist(table, column):# noqa
                    dAdapter.deleteColumnFromTable(table, column)
        else:
            pass

        i = i + 1
