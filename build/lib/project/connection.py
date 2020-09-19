import mysql.connector


class SQL:
    def __init__(self, host, user, password, database=""):
        self.db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        self.cursor = self.db.cursor()

    def execute(self, query: str, val = ""):
        if val == "":
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, val)

    def executemany(self, queries, val):
        self.cursor.executemany(queries, val)

    def commit(self):
        self.db.commit()

    def fetch(self):
        return self.cursor.fetchall()

    def rowcount(self):
        return self.cursor.rowcount()

    def lastrowid(self):
        self.cursor.lastrowid()
