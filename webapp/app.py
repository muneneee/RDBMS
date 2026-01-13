from flask import Flask, request, render_template
from db.database import Database
from db.table import Column

app = Flask(__name__)
db = Database()

# Create table
db.create_table("todos", [Column("id", "INT", primary=True), Column("task", "TEXT")])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        id = len(db.select_all("todos")) + 1
        db.insert("todos", {"id": id, "task": task})
    todos = db.select_all("todos")
    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)
