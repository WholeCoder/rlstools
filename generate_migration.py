#!/usr/bin/python3
import sys
from sqlite_adapter import SqliteDatabaseAdapter

dAdapter = SqliteDatabaseAdapter.getInstance()

print("Command == "+sys.argv[0])
print("app directory name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

next_available_database_version = dAdapter.getNextDatabaseVersionNumber()
 
new_view = open(sys.argv[1]+"/"+next_available_database_version + "_migration",'w')
new_view.write("upgrade\n")
new_view.write("add table "+sys.argv[2]+"\n")

count = 3
while count < len(sys.argv):
    new_view.write("add column "+sys.argv[2]+" "+sys.argv[count].split(":")[0]+"\n")
    count += 1

new_view.write("\n\ndowngrade\n")
count = 3
while count < len(sys.argv):
    new_view.write("remove column "+sys.argv[2]+" "+sys.argv[count].split(":")[0]+"\n")
    count += 1

new_view.write("remove table "+sys.argv[2]+"\n")
new_view.close()
