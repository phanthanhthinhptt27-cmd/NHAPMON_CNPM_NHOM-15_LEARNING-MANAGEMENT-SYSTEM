"""
Unit Test cho Lop FineCalculator (Hoat dong 3 - Chuong 4)
Ap dung chat che cau truc AAA (Arrange - Act - Assert)
Quy tac: 5.000d/ngay. Neu qua han > 10 ngay, phat them 20%.
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.library.fine_calculator import FineCalculator


class TestFineCalculator(unittest.TestCase):
    """Kiem thu chuc nang tinh tien phat muon sach qua han."""

    def setUp(self):
        """Khoi tao doi tuong FineCalculator truoc moi test case."""
        self.calc = FineCalculator()

    # ===== TEST CASE 1: Tra sach dung han (0 ngay) -> Mong doi: 0d =====
    def test_no_fine(self):
        """TC1: Tra sach dung han (daysOverdue = 0) -> Tien phat = 0d."""
        # 1. Arrange (Chuan bi du lieu dau vao va ket qua ky vong)
        days = 0
        expected = 0.0

        # 2. Act (Thuc thi ham can test)
        actual = self.calc.calculate(days)

        # 3. Assert (Kiem chung ket qua)
        self.assertEqual(actual, expected, "Tra sach dung han (0 ngay) khong bi phat tien")

    # ===== TEST CASE 2: Qua han binh thuong (5 ngay) -> Mong doi: 25.000d =====
    def test_normal_fine(self):
        """TC2: Qua han 5 ngay (<= 10 ngay) -> 5 * 5000 = 25.000d."""
        # 1. Arrange
        days = 5
        expected = 25000.0

        # 2. Act
        actual = self.calc.calculate(days)

        # 3. Assert
        self.assertEqual(actual, expected, "Qua han 5 ngay phai phat dung 25.000d")

    # ===== TEST CASE 3: Qua han nang (11 ngay) -> Mong doi: (11*5000)*1.2 = 66.000d =====
    def test_heavy_fine(self):
        """TC3: Qua han 11 ngay (> 10 ngay) -> (11 * 5000) * 1.2 = 66.000d."""
        # 1. Arrange
        days = 11
        expected = 66000.0

        # 2. Act
        actual = self.calc.calculate(days)

        # 3. Assert
        self.assertEqual(actual, expected, "Qua han 11 ngay phai phat 66.000d (phat them 20%)")

    # ===== TEST CASE 4 (Test bien): Dung 10 ngay -> Chua vuot qua 10 ngay =====
    def test_boundary_ten_days(self):
        """TC4: Qua han dung 10 ngay -> 10 * 5000 = 50.000d (chua vuot moc 10 ngay)."""
        # 1. Arrange
        days = 10
        expected = 50000.0

        # 2. Act
        actual = self.calc.calculate(days)

        # 3. Assert
        self.assertEqual(actual, expected, "Dung 10 ngay khong bi phat them 20%")

    # ===== TEST CASE 5 (Test bien am): So ngay am -> Mong doi: 0d =====
    def test_negative_days(self):
        """TC5: So ngay qua han la so am (-3 ngay) -> Tien phat = 0d."""
        # 1. Arrange
        days = -3
        expected = 0.0

        # 2. Act
        actual = self.calc.calculate(days)

        # 3. Assert
        self.assertEqual(actual, expected, "So ngay am phai tra ve 0d")


if __name__ == '__main__':
    unittest.main()
