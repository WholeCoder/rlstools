#!/usr/bin/python3
import sys
import os
from sqlite_adapter import SqliteDatabaseAdapter

dAdapter = SqliteDatabaseAdapter.getInstance()

print("Command == "+sys.argv[0])
print("app directory name = " + sys.argv[1])
print("scaffold name = " + sys.argv[2])

next_available_database_version = dAdapter.getNextDatabaseVersionNumber()

num_list = []
files = os.listdir(".")
for f in files:
    part = f.split("_")[0]
    num_list.append(part)

num_list.sort(reverse=True)
max = "000"
if len(num_list) > 0:
    nn = int(num_list[0]) + 1
    if nn < 10:
        max = "00" + str(nn)
    elif nn < 100:
        max = "0" + str(nn)
    else:
        max = str(nn)
next_available_database_version = max

with open(sys.argv[1]+"/"+next_available_database_version + "_migration", 'w') as new_view: # noqa
    new_view.write("upgrade\n")
    new_view.write("add table "+sys.argv[2]+"\n")

    count = 3
    while count < len(sys.argv):
        new_view.write("add column "+sys.argv[2]+" "+sys.argv[count].split(":")[0]+"\n")# noqa
        count += 1

    new_view.write("\n\ndowngrade\n")
    count = 3
    while count < len(sys.argv):
        new_view.write("remove column "+sys.argv[2]+" "+sys.argv[count].split(":")[0]+"\n")# noqa
        count += 1

    new_view.write("remove table "+sys.argv[2]+"\n")
