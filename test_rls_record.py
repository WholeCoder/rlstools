from sqlite_adapter import SqliteDatabaseAdapter
from person_rls_record import Person
import unittest
import os

class RlsRecordTestCase(unittest.TestCase):
    def setUp(self):
        database_path = "my_test_database.db"
        try:
            #print("Trying to remove "+database_path)
            os.remove(database_path)
        except:
            pass
            #print("Error deleting "+database_path+" this isn't really an error.")
        self.dAdapter = SqliteDatabaseAdapter.getTestInstance()
    
    def test_insert_data_into_rls_record_object(self):
        self.dAdapter.createTable("Person")
        self.dAdapter.addColumn("Person","first_name")
        self.dAdapter.addColumn("Person","last_name")

        insertDictionary = {"first_name":"Ruben","last_name":"Pierich"}
        Person(self.dAdapter).create(insertDictionary)

        insertDictionary = {"first_name":"Shannon","last_name":"Underkoffler"}
        Person(self.dAdapter).create(insertDictionary)

        rows = Person(self.dAdapter).findAll()
        #print("row 1 == " + str(rows[0]))

        self.assertTrue(rows[0]['first_name'] == 'Ruben')
        self.assertTrue(rows[0]['last_name'] == 'Pierich')

if __name__ == '__main__':
    unittest.main()

