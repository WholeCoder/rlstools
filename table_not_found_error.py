from sqlite3 import OperationalError


class TableNotFoundError(OperationalError):
    def __init__(self, msg):
        self.msg = msg
