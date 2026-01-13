# Todo App with Custom RDBMS

A simple Todo web app built on a **custom in-memory RDBMS** demonstrating **full CRUD operations** (Create, Read, Update, Delete) and basic **JOIN support**.

## Features

- **Custom Database**
  - Define tables with columns and data types (`INT`, `TEXT`)
  - Primary key support
  - Insert, select, update, delete rows
  - Basic JOINs between tables

- **Web App**
  - Add, update, and delete tasks
  - Update forms appear inline
  - Built with Flask

- **REPL**
  - Interact with the database via SQL-like commands:
    ```text
    CREATE TABLE users (id INT PRIMARY, name TEXT);
    CREATE TABLE todos (id INT PRIMARY, task TEXT, user_id INT);
    INSERT INTO users (id, name) VALUES (1, "Kevin");
    INSERT INTO todos (id, task, user_id) VALUES (1, "Buy milk", 1);
    SELECT * FROM todos;
    UPDATE todos SET task="Buy bread" WHERE id=1;
    DELETE FROM todos WHERE id=1;
    JOIN todos users ON user_id=id;
    ```

## Installation

```bash
git clone [(https://github.com/muneneee/RDBMS.git)]
cd RDBMS
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install flask
python -m webapp.app       # Run web app
python repl.py             # Run REPL
