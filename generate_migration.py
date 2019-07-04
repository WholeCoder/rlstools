#!/usr/bin/python3
import sys
import ../../sqlite_adapter import SqliteDatabaseAdapter

dAdapter = SqliteDatabaseAdapter.getInstance()

print("Command == "+sys.argv[0])
print("app directory name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

next_available_database_verion = dSdapter.getNewDatabaseVersionNumber()
if next_avaiable_database_version < 10:
    nn = "00"+str(next_avaiable_database_version)
elif next_avaiable_database_version < 100
    nn = "0"+str(next_avaiable_database_version)
else
    nn = str(next_avaiable_database_version)

new_view = open(sys.argv[1]+"/"+nn+"_migration",'w')
new_view.write("upgrade\n")
new_view.write("add table "+sys.argv[2]+"\n"

count = 3
while count < len(sys.argv):
    new_view.write("add column "+argv[2]+" "+sys.argv[count]+"\n")
    count += 1

new_view.write("\n\ndowngrade")
count = 3
while count < len(sys.argv):
    new_view.write("remove column "+argv[2]+" "+sys.argv[count]+"\n")
    count += 1

new_view.write("remove table "+argv[2])
new_view.close()
