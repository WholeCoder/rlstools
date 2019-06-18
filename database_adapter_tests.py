from sqlite_adapter import SqliteDatabaseAdapter
import unittest
import os


class DatabaseAdapterTestCase(unittest.TestCase):
    def setUp(self):
        database_path = "my_test_database.db"
        try:
            print("Trying to remove "+database_path)
            os.remove(database_path)
        except:
            print("Error deleting "+database_path+" this isn't really an error.")
        self.dAdapter = SqliteDatabaseAdapter(database_path)
    
    def test_add_person_table_without_columns(self):
        self.dAdapter.createTable("Person")
        self.assertTrue(self.dAdapter.doesTableExist("Person"))

    def test_if_can_drop_table(self):
        self.dAdapter.createTable("Person")
        self.assertTrue(self.dAdapter.doesTableExist("Person"))
        self.dAdapter.dropTable("Person")
        self.assertFalse(self.dAdapter.doesTableExist("Person"))

    def test_if_can_add_column_to_office_table(self):
        self.dAdapter.createTable("Office")
        self.dAdapter.addColumn("Office","zipcode")
        self.assertTrue(self.dAdapter.doesColumnExist("Office", "zipcode"))
    
    def test_if_can_drop_column(self):
        self.dAdapter.createTable("Office")
        self.dAdapter.addColumn("Office","zipcode")
        self.dAdapter.deleteColumnFromTable("Office","zipcode")
        self.assertFalse(self.dAdapter.doesColumnExist("Office", "zipcode"))


if __name__ == '__main__':
    unittest.main()

