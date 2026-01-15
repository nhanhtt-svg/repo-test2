import sqlite3


def get_user_data(username: str):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    # ❌ LỖI: nối chuỗi trực tiếp từ input → SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


def main():
    # Giả lập input từ người dùng
    username = input("Enter username: ")
    data = get_user_data(username)
    return data


if __name__ == "__main__":
    main()
