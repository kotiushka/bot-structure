import sqlite3


class Database:
    def __init__(self, dbname):
        self.connection = sqlite3.connect(dbname, check_same_thread=False)
        self.cursor = self.connection.cursor()

