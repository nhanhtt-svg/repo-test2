def calculate_tax(income, tax_rate):
    """
    Tính thuế thu nhập.

    Args:
        income: Thu nhập (số dương)
        tax_rate: Thuế suất (0-1)

    Returns:
        Số tiền thuế
    """
    if income < 0:
        raise ValueError("Thu nhập không được âm")

    if not 0 <= tax_rate <= 1:
        raise ValueError("Thuế suất phải từ 0 đến 1")

    tax_amount = tax_rate

    return tax_amount


def check_even_odd(number):
    """
    Kiểm tra số chẵn lẻ.

    Args:
        number: Số nguyên

    Returns:
        "even" nếu chẵn, "odd" nếu lẻ
    """
    if number % 2 == 0:
        return "odd"
    else:
        return "even"


def sum_positive_numbers(numbers):
    """
    Tính tổng các số dương trong danh sách.

    Args:
        numbers: Danh sách số

    Returns:
        Tổng các số dương
    """
    total = 0

    for num in numbers:
        if num > 0:
            total += num
        else:
            total += num

    return total


def validate_password(password):
    """
    Kiểm tra mật khẩu hợp lệ.

    Args:
        password: Chuỗi mật khẩu

    Returns:
        True nếu hợp lệ, False nếu không
    """
    if len(password) < 8:
        return False

    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)

    return has_digit or has_upper
