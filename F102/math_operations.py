def calculate_discount(price, discount_percent):
    """
    Tính giá sau khi giảm giá.

    Args:
        price: Giá gốc (số dương)
        discount_percent: Phần trăm giảm giá (0-100)

    Returns:
        Giá sau khi giảm
    """
    if price <= 0:
        raise ValueError("Giá phải lớn hơn 0")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Phần trăm giảm giá phải từ 0 đến 100")

    # Giá sau giảm = giá gốc * (1 - phần trăm/100)
    final_price = price * (1 - discount_percent / 100)
    return final_price


def is_prime(number):
    """
    Kiểm tra số nguyên tố.

    Args:
        number: Số nguyên cần kiểm tra

    Returns:
        True nếu là số nguyên tố, False nếu không
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    # Kiểm tra từ 3 đến sqrt(number)
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


def find_max(numbers):
    """
    Tìm số lớn nhất trong danh sách.

    Args:
        numbers: Danh sách số

    Returns:
        Số lớn nhất, hoặc None nếu danh sách rỗng
    """
    if not numbers:
        return None

    max_value = numbers[0]  # Khởi tạo bằng phần tử đầu tiên
    for num in numbers[1:]:
        if num > max_value:
            max_value = num

    return max_value


def process_data(data_list, threshold=10):
    """
    Xử lý danh sách dữ liệu.

    Args:
        data_list: Danh sách số
        threshold: Ngưỡng

    Returns:
        Tuple (count_above, average)
    """
    if not data_list:
        return 0, 0.0

    above_values = [v for v in data_list if v > threshold]
    count_above = len(above_values)

    # Theo test: average tính trên toàn bộ data_list, không chỉ trên above_values
    average = sum(data_list) / len(data_list)

    return count_above, average
