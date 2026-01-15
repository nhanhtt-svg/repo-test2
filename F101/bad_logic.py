def calculate_tax(income: float, rate: float) -> float:
    if income < 0:
        raise ValueError("Income must be non-negative")
    if rate < 0 or rate > 1:
        raise ValueError("Tax rate must be between 0 and 1")
    return income * rate


def check_even_odd(n: int) -> str:
    return "even" if n % 2 == 0 else "odd"


def sum_positive_numbers(numbers: list[int]) -> int:
    return sum(n for n in numbers if n > 0)


def validate_password(password: str) -> bool:
    if len(password) < 6:
        return False
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    return has_digit and has_upper
