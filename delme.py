from sqlite_adapter import SqliteDatabaseAdapter


print(SqliteDatabaseAdapter.getTestInstance().conn)
SqliteDatabaseAdapter.getInstance().createTable("Person")
dAdapter = SqliteDatabaseAdapter.getInstance()

dAdapter.addColumn("Person","zipcode")
