"""
Unit Test - Phan he Quan ly Khoa hoc & Giang day (LMS)
Thanh vien: Tran Duc Duy - MSSV: 25S1020023
Ap dung cau truc AAA (Arrange - Act - Assert)
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.lms.course_management import CourseManager


class TestCourseManagement(unittest.TestCase):
    """Test module quan ly khoa hoc - Tran Duc Duy."""

    def setUp(self):
        """Khoi tao CourseManager truoc moi test case."""
        self.manager = CourseManager()

    # ===== TEST CASE 1: Them khoa hoc moi thanh cong =====
    def test_add_course_success(self):
        """TC1: Them khoa hoc moi voi thong tin hop le -> Thanh cong."""
        # 1. Arrange
        course_id = "CS101"
        name = "Nhap mon Cong nghe Phan mem"
        code = "NMCNPM"
        credits = 3

        # 2. Act
        result = self.manager.add_course(course_id, name, code, credits)

        # 3. Assert
        self.assertTrue(result, "Them khoa hoc moi phai thanh cong")
        self.assertIn(course_id, self.manager.courses, "Khoa hoc phai ton tai trong danh sach")

    # ===== TEST CASE 2: Them khoa hoc bi trung ma dinh danh =====
    def test_add_course_duplicate_id_fails(self):
        """TC2: Them khoa hoc voi ma dinh danh da ton tai -> That bai."""
        # 1. Arrange
        self.manager.add_course("CS101", "Mon A", "MA", 3)

        # 2. Act
        result = self.manager.add_course("CS101", "Mon B", "MB", 2)

        # 3. Assert
        self.assertFalse(result, "Them khoa hoc trung ma phai that bai")

    # ===== TEST CASE 3: Xoa khoa hoc thanh cong =====
    def test_delete_course_success(self):
        """TC3: Xoa khoa hoc da ton tai -> Thanh cong."""
        # 1. Arrange
        self.manager.add_course("CS102", "Lap trinh Python", "LTP", 4)

        # 2. Act
        result = self.manager.delete_course("CS102")

        # 3. Assert
        self.assertTrue(result, "Xoa khoa hoc ton tai phai thanh cong")
        self.assertNotIn("CS102", self.manager.courses, "Khoa hoc phai bi xoa khoi danh sach")

    # ===== TEST CASE 4: Xoa khoa hoc khong ton tai =====
    def test_delete_course_not_found_fails(self):
        """TC4: Xoa khoa hoc khong ton tai trong he thong -> That bai."""
        # 1. Arrange
        non_existent_id = "FAKE999"

        # 2. Act
        result = self.manager.delete_course(non_existent_id)

        # 3. Assert
        self.assertFalse(result, "Xoa khoa hoc khong ton tai phai that bai")


if __name__ == '__main__':
    unittest.main()
