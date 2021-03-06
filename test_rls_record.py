from sqlite_adapter import SqliteDatabaseAdapter
from person_rls_record import Person
import unittest
import os


class RlsRecordTestCase(unittest.TestCase):
    def setUp(self):
        database_path = "my_test_db.db"
        try:
            os.remove(database_path)
        except IOError as err:
            print("I/O error: {0}".format(err))
        self.dAdapter = SqliteDatabaseAdapter.getTestInstance()
        print(self.dAdapter)

    def test_insert_data_into_rls_record_object(self):
        self.dAdapter.createTable("Person")
        self.dAdapter.addColumn("Person", "first_name", "string")
        self.dAdapter.addColumn("Person", "last_name", "string")

        insertDictionary = {"first_name": "Ruben", "last_name": "Pierich"}
        Person.create(insertDictionary)

        insertDictionary = {"first_name": "Shannon", "last_name": "Underkoffler"}# noqa
        Person.create(insertDictionary)

        rows = Person.findAll()

        self.assertTrue(rows[0]['first_name'] == 'Ruben')
        self.assertTrue(rows[0]['last_name'] == 'Pierich')


if __name__ == '__main__':
    unittest.main()
