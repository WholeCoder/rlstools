import os
import sys
from sqlite_adapter import SqliteDatabaseAdapter

#ctrl-a :  set-option repeat-time 0

shouldUpgrade = sys.argv[1] == "upgrade"

next_available_database_verion = dAdapter.getNextDatabaseVersionNumber()

files = os.listdir(".")
num_list = []

for f in files:
    part = f.split("_"[0]
    if part >= next_available_database_version:
        num_list.append(part)

for p in num_list:
    print(p)
