import pickle
import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id")  # User-controlled input
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # f-string injection
    cursor.execute(query)  # Sink rõ ràng
    return "Done"


# 2. Unsafe deserialization với remote input


@app.route("/load")
def load_pickle():
    data = request.data  # User-controlled bytes
    obj = pickle.loads(data)  # Unsafe sink với remote source
    return str(obj)
