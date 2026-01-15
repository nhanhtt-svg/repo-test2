import sqlite3
import sys


def get_user_data(username: str):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    # ❌ SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


if __name__ == "__main__":
    # Lấy input từ sys.argv (CodeQL coi là tainted source)
    if len(sys.argv) > 1:
        user = sys.argv[1]
        get_user_data(user)
