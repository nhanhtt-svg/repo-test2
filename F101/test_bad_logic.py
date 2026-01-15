import unittest

from F101.bad_logic import calculate_tax, check_even_odd, sum_positive_numbers, validate_password


class TestCalculateTax(unittest.TestCase):
    """Test tính thuế"""

    def test_tax_calculation(self):
        """Thu nhập 1000, thuế suất 0.1 => thuế 100"""
        result = calculate_tax(1000, 0.1)
        self.assertEqual(result, 100)

    def test_tax_zero_rate(self):
        """Thuế suất 0 => thuế 0"""
        result = calculate_tax(500, 0)
        self.assertEqual(result, 0)

    def test_tax_high_rate(self):
        """Thuế suất 0.5 => thuế nửa thu nhập"""
        result = calculate_tax(200, 0.5)
        self.assertEqual(result, 100)

    def test_invalid_income(self):
        """Thu nhập âm phải raise ValueError"""
        with self.assertRaises(ValueError):
            calculate_tax(-100, 0.1)

    def test_invalid_tax_rate(self):
        """Thuế suất > 1 phải raise ValueError"""
        with self.assertRaises(ValueError):
            calculate_tax(100, 1.5)


class TestCheckEvenOdd(unittest.TestCase):
    """Test kiểm tra chẵn lẻ"""

    def test_even_numbers(self):
        """Số chẵn phải trả "even" """
        self.assertEqual(check_even_odd(2), "even")
        self.assertEqual(check_even_odd(10), "even")
        self.assertEqual(check_even_odd(0), "even")

    def test_odd_numbers(self):
        """Số lẻ phải trả "odd" """
        self.assertEqual(check_even_odd(3), "odd")
        self.assertEqual(check_even_odd(7), "odd")
        self.assertEqual(check_even_odd(-1), "odd")


class TestSumPositiveNumbers(unittest.TestCase):
    """Test tính tổng số dương"""

    def test_all_positive(self):
        """Tất cả số dương"""
        self.assertEqual(sum_positive_numbers([1, 2, 3, 4]), 10)

    def test_mixed_numbers(self):
        """Hỗn hợp âm dương - HÀM SAI"""
        self.assertEqual(sum_positive_numbers([1, -2, 3, 4]), 5)

    def test_all_negative(self):
        """Tất cả số âm"""
        self.assertEqual(sum_positive_numbers([-1, -2, -3]), 0)

    def test_empty_list(self):
        """Danh sách rỗng"""
        self.assertEqual(sum_positive_numbers([]), 0)


class TestValidatePassword(unittest.TestCase):
    """Test kiểm tra mật khẩu"""

    def test_valid_password(self):
        """Mật khẩu hợp lệ: có số VÀ chữ hoa"""
        self.assertTrue(validate_password("Pass1234"))
        self.assertTrue(validate_password("ABCdef123"))

    def test_invalid_password_no_digit(self):
        """Không có số -> không hợp lệ"""
        self.assertFalse(validate_password("Password"))

    def test_invalid_password_no_upper(self):
        """Không có chữ hoa -> không hợp lệ"""
        self.assertFalse(validate_password("password123"))

    def test_invalid_password_too_short(self):
        """Quá ngắn -> không hợp lệ"""
        self.assertFalse(validate_password("Ab1"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
