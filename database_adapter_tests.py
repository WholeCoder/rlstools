from sqlite_adapter import SqliteDatabaseAdapter
import unittest
import os


class DatabaseAdapterTestCase(unittest.TestCase):
    def setUp(self):
        database_path = "my_test_database.db"
        try:
            #print("Trying to remove "+database_path)
            os.remove(database_path)
        except:
            pass
            #print("Error deleting "+database_path+" this isn't really an error.")
        self.dAdapter = SqliteDatabaseAdapter.getTestInstance()
        if self.dAdapter.doesTableExist("db_versions"):
            self.dAdapter.dropTable("db_versions")

        print("sqllitedatabaseadapter ->>>>>>>>>>>>>>>>>>"+str(SqliteDatabaseAdapter.getTestInstance())
                )
    def test_if_get_next_version_of_database(self):
        nn = self.dAdapter.getNextDatabaseVersionNumber()
        self.assertTrue(nn == "000")
        nn = self.dAdapter.getNextDatabaseVersionNumber()
        self.assertTrue(nn == "001")
        nn2 = self.dAdapter.getMostRecentDatabaseVersionNumber()
        print("nn2 == " + nn2)
        self.assertTrue(nn2 == "001")
        nn2 = self.dAdapter.getMostRecentDatabaseVersionNumber()
        self.assertTrue(nn2 == "001")


    def test_if_columns_returned(self):
        self.dAdapter.createTable("Office")
        self.dAdapter.addColumn("Office","zipcode")
        self.dAdapter.addColumn("Office","city")
        columns = self.dAdapter.getColumnsAsList("Office")
        print("list of Office columns == "+str(columns))
        self.assertTrue("zipcode" in columns)
        self.assertTrue("city" in columns)

    def test_if_delete_column_brings_back_a_deleted_column(self):
        self.dAdapter.createTable("Person")
        self.dAdapter.addColumn("Person","zipcode")
        self.assertTrue(self.dAdapter.doesTableExist("Person"))
        self.dAdapter.dropTable("Person")
        self.dAdapter.deleteColumnFromTable("Person","zipcode")
        self.assertFalse(self.dAdapter.doesTableExist("Person"))

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


