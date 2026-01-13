# repl.py
from db.database import Database
from db.table import Column

db = Database()

def parse_create(cmd):
    # Example: CREATE TABLE users (id INT PRIMARY, name TEXT);
    cmd = cmd.replace("CREATE TABLE", "").strip()
    name, cols = cmd.split("(", 1)
    name = name.strip()
    cols = cols.rstrip(");").split(",")
    columns = []
    for c in cols:
        parts = c.strip().split()
        col_name = parts[0]
        dtype = parts[1]
        primary = "PRIMARY" in parts
        columns.append(Column(col_name, dtype, primary))
    db.create_table(name, columns)
    print(f"Table {name} created")

def parse_insert(cmd):
    # Example: INSERT INTO users (id, name) VALUES (1, "Kevin");
    cmd = cmd.replace("INSERT INTO", "").strip()
    table_part, values_part = cmd.split("VALUES")
    table_name = table_part.split("(")[0].strip()
    cols = table_part.split("(")[1].rstrip(")").split(",")
    cols = [c.strip() for c in cols]
    vals = values_part.strip().lstrip("(").rstrip(");").split(",")
    vals = [v.strip().strip('"') for v in vals]
    row = dict(zip(cols, vals))
    db.insert(table_name, row)
    print("Row inserted")

def parse_join(cmd):
    # Example: JOIN users orders ON id = user_id;
    cmd = cmd.replace("JOIN", "").strip().rstrip(";")

    tables_part, condition_part = cmd.split("ON")

    table1, table2 = tables_part.strip().split()

    col1, col2 = condition_part.strip().split("=")
    col1 = col1.strip()
    col2 = col2.strip()

    results = db.join_tables(table1, table2, col1, col2)

    for r in results:
        print(r)


def repl():
    while True:
        cmd = input("> ")
        if cmd.lower() in ["exit", "quit"]:
            break
        elif cmd.startswith("CREATE TABLE"):
            parse_create(cmd)
        elif cmd.startswith("INSERT INTO"):
            parse_insert(cmd)
        elif cmd.startswith("SELECT * FROM"):
            table_name = cmd.replace("SELECT * FROM", "").strip().rstrip(";")
            rows = db.select_all(table_name)
            for r in rows:
                print(r)
        elif cmd.startswith("JOIN"):
            parse_join(cmd)
        else:
            print("Unknown command")

if __name__ == "__main__":
    repl()
