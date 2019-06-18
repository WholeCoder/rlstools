from sqlite_adapter import SqliteDatabaseAdapter
import unittest
import os


class DatabaseAdapterTestCase(unittest.TestCase):
    def setUp(self):
        database_path = "my_test_database.db"
        os.remove(database_path)
        self.dAdapter = SqliteDatabaseAdapter(database_path)
    
    def test_add_person_table_without_columns(self):
        self.dAdapter.createTable("Person")
        self.assertTrue(self.dAdapter.doesTableExist("Person"))

if __name__ == '__main__':
    unittest.main()

