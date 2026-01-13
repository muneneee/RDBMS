from .table import Table, Column

class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, columns):
        if name in self.tables:
            raise ValueError("Table already exists")
        self.tables[name] = Table(name, columns)

    def insert(self, table_name, row):
        if table_name not in self.tables:
            raise ValueError("Table does not exist")
        self.tables[table_name].insert(row)

    def select_all(self, table_name):
        if table_name not in self.tables:
            raise ValueError("Table does not exist")
        return self.tables[table_name].rows

