# math_operations.py
# File có lỗi LOGIC nhưng format/style hoàn toàn đúng

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

    # LỖI LOGIC: Sai công thức tính giảm giá
    # Đúng phải là: price * (100 - discount_percent) / 100
    # Nhưng code này làm: price * discount_percent / 100 (chỉ tính phần giảm, chưa trừ)
    discount_amount = price * discount_percent / 100

    # LỖI LOGIC: Thiếu phép trừ
    # Đáng lẽ phải: final_price = price - discount_amount
    final_price = discount_amount  # SAI: Chỉ bằng số tiền giảm giá

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

    # LỖI LOGIC: Chỉ kiểm tra đến sqrt(number) nhưng code lại dùng number // 2
    # và thiếu xử lý số 2
    for i in range(2, number // 2):
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

    # LỖI LOGIC: Khởi tạo max_value = 0, sẽ sai với danh sách toàn số âm
    max_value = 0

    for num in numbers:
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

    count_above = 0
    total = 0

    # LỖI LOGIC: Đếm và tính tổng nhưng không chia đúng cho average
    for value in data_list:
        if value > threshold:
            count_above += 1
        total += value

    # LỖI LOGIC: Tính average cho toàn bộ data_list, không chỉ phần > threshold
    average = total / len(data_list)

    return count_above, average
