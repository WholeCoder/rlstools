from base_rls_record import BaseRlsRecord
import atexit
import sqlite3


class Person(BaseRlsRecord):
    def __init__(self,dAdapter):
        super().__init__(dAdapter)

    def cleanup(self):
        self.conn.close()

