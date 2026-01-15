import sqlite3
import sys


def delete_user_account(username: str) -> int:
    """Xóa tài khoản user - DANGEROUS VERSION với SQL Injection"""
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # ❌ SQL Injection NGUY HIỂM: Có thể xóa toàn bộ bảng
    query = f"DELETE FROM users WHERE username = '{username}'"
    cursor.execute(query)
    conn.commit()  # Thay đổi được lưu vào database

    affected = cursor.rowcount
    conn.close()

    print(f"Đã xóa {affected} tài khoản")
    return affected


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        delete_user_account(user_input)
