from sqlite_adapter import SqliteDatabaseAdapter

nn = SqliteDatabaseAdapter.getInstance().getNextDatabaseVersionNumber()
print(nn)
