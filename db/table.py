class Column:
    def __init__(self, name, dtype, primary=False, unique=False):
        self.name = name
        self.dtype = dtype
        self.primary = primary
        self.unique = unique

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.rows = []
        self.pk_index = {}  # Dictionary for primary key fast lookup
        self.unique_index = {}  # Dictionary for unique keys

    def insert(self, row):
        # Check primary key
        for col in self.columns:
            if col.primary:
                pk_val = row[col.name]
                if pk_val in self.pk_index:
                    raise ValueError(f"Duplicate primary key: {pk_val}")
                self.pk_index[pk_val] = row
            if col.unique:
                u_val = row[col.name]
                if u_val in self.unique_index:
                    raise ValueError(f"Duplicate unique value: {u_val}")
                self.unique_index[u_val] = row
        self.rows.append(row)
