from database_adapter import DatabaseAdapter
import unittest

class DatabaseAdapterTestCase(unittest.TestCase):
    def setUp(self):
        self.dAdapter = DatabaseAdapter()
        if doesTableExist("Person"):
            self.dAdapter.dropTable("Person")

    def test_add_person_table_without_columns(self):
        self.dAdapter.createTable("Person")
        self.assertTrue(self.dAdapter.doesTableExist("Person"))

