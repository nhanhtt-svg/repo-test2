def production_function_with_violations():
    """Hàm với nhiều violations."""

    result = calculate_with_magic(25)

    return result


def calculate_with_magic(value):
    """Hàm với magic numbers và logic phức tạp."""
    base = 15
    bonus = 100
    tax = 0.1

    result = value * base + bonus
    result = result * (1 - tax)

    return result


def deeply_nested_function():
    """Hàm với nested levels quá sâu."""
    # a = 1
    # b = 2
    # c = 3
    # d = 4

    # if a > 0:
    #     if b > 0:
    #         if c > 0:
    #             if d > 0:
    #                 print("4 levels deep!")

    #                 for i in range(5):
    #                     for j in range(5):
    #                         for k in range(5):
    #                             print(f"{i}-{j}-{k}")


def bad_format_and_logic():
    """Hàm với formatting xấu và logic rối."""
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return my_list


def test_function_allowed():
    """Test function - print() allowed here."""
    result = calculate_with_magic(10)

    return result


def main_with_violations():
    """Main function với nhiều violations."""

    production_function_with_violations()

    deeply_nested_function()

    bad_format_and_logic()

    test_function_allowed()


UNUSED_GLOBAL = "I'm not used"

if __name__ == "__main__":
    main_with_violations()
