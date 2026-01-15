# test_math_operations.py
import pytest
from math_operations import calculate_discount, find_max, is_prime, process_data


class TestCalculateDiscount:
    """Test tính giảm giá"""

    def test_discount_50_percent(self):
        """Giảm 50% giá 100 => 50"""
        result = calculate_discount(100, 50)
        # Đúng phải là 50, nhưng hàm sai sẽ trả về 50 (tình cờ đúng vì 50% của 100 = 50)
        assert result == 50  # Test này pass nhưng hàm vẫn sai!

    def test_discount_20_percent(self):
        """Giảm 20% giá 100 => 80"""
        result = calculate_discount(100, 20)
        # Đúng: 80, Hàm sai: 20 (20% của 100)
        assert result == 80  # Test này sẽ FAIL

    def test_discount_0_percent(self):
        """Giảm 0% giá 100 => 100"""
        result = calculate_discount(100, 0)
        assert result == 100  # Sẽ FAIL (hàm trả về 0)

    def test_invalid_price(self):
        """Giá âm phải raise ValueError"""
        with pytest.raises(ValueError):
            calculate_discount(-10, 20)

    def test_invalid_discount(self):
        """Discount > 100 phải raise ValueError"""
        with pytest.raises(ValueError):
            calculate_discount(100, 150)


class TestIsPrime:
    """Test kiểm tra số nguyên tố"""

    def test_prime_numbers(self):
        """Các số nguyên tố"""
        assert is_prime(2)  # Sẽ FAIL (hàm kiểm tra range(2, 1) rỗng)
        assert is_prime(3)  # Sẽ FAIL
        assert is_prime(5)
        assert is_prime(7)

    def test_non_prime_numbers(self):
        """Các số không phải nguyên tố"""
        assert not is_prime(1)
        assert not is_prime(4)  # Sẽ FAIL (4 % 2 == 0 nhưng range(2, 2) rỗng)
        assert not is_prime(9)  # Sẽ FAIL
        assert not is_prime(15)  # Sẽ FAIL

    def test_negative_numbers(self):
        """Số âm không phải nguyên tố"""
        assert not is_prime(-1)
        assert not is_prime(-5)


class TestFindMax:
    """Test tìm số lớn nhất"""

    def test_positive_numbers(self):
        """Danh sách số dương"""
        assert find_max([1, 5, 3, 9, 2]) == 9

    def test_negative_numbers(self):
        """Danh sách toàn số âm - HÀM SAI"""
        # Hàm khởi tạo max_value = 0, sẽ luôn trả về 0 với số âm
        assert find_max([-5, -10, -3, -1]) == -1  # Sẽ FAIL (hàm trả về 0)

    def test_mixed_numbers(self):
        """Danh sách số âm dương lẫn lộn"""
        assert find_max([-5, 10, -3, 8]) == 10

    def test_empty_list(self):
        """Danh sách rỗng trả về None"""
        assert find_max([]) is None

    def test_single_element(self):
        """Danh sách 1 phần tử"""
        assert find_max([42]) == 42
        assert find_max([-7]) == -7  # Sẽ FAIL (hàm trả về 0)


class TestProcessData:
    """Test xử lý dữ liệu"""

    def test_basic_functionality(self):
        """Test cơ bản"""
        data = [5, 15, 25, 10, 20]
        count, avg = process_data(data, threshold=10)
        # count_above = 3 (15, 25, 20)
        # average = (5+15+25+10+20)/5 = 75/5 = 15
        assert count == 3
        assert avg == 15.0

    def test_all_below_threshold(self):
        """Tất cả dưới ngưỡng"""
        data = [1, 2, 3, 4, 5]
        count, avg = process_data(data, threshold=10)
        assert count == 0
        assert avg == 3.0  # (1+2+3+4+5)/5

    def test_all_above_threshold(self):
        """Tất cả trên ngưỡng"""
        data = [15, 20, 25]
        count, avg = process_data(data, threshold=10)
        assert count == 3
        assert avg == 20.0  # (15+20+25)/3

    def test_empty_data(self):
        """Danh sách rỗng"""
        count, avg = process_data([])
        assert count == 0
        assert avg == 0.0


# Test thêm để phát hiện lỗi tinh vi
def test_discount_edge_cases():
    """Test các trường hợp biên của discount"""
    # 100% discount => giá 0
    assert calculate_discount(100, 100) == 0  # Sẽ FAIL (hàm trả về 100)

    # 1% discount trên giá lớn
    assert calculate_discount(1000, 1) == 990  # Sẽ FAIL (hàm trả về 10)


def test_prime_edge_cases():
    """Test biên số nguyên tố"""
    # Số 2 là số nguyên tố chẵn duy nhất
    assert is_prime(2)  # Sẽ FAIL

    # Số 1 không phải nguyên tố
    assert not is_prime(1)

    # Số lớn không nguyên tố
    assert not is_prime(49)  # 49 = 7*7, Sẽ FAIL


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
