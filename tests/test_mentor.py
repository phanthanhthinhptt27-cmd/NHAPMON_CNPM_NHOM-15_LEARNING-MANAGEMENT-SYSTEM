"""
Unit Test - Phan he Ket noi Mentor - Mentee
Thanh vien: Phan Van Hao
Ap dung cau truc AAA (Arrange - Act - Assert)
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.mentor.mentor_management import MentorManager


class TestMentorManagement(unittest.TestCase):
    """Test module ket noi Mentor-Mentee - Phan Van Hao."""

    def setUp(self):
        """Khoi tao MentorManager truoc moi test case."""
        self.manager = MentorManager()

    # ===== TEST CASE 1: Tim kiem mentor theo ky nang thanh cong =====
    def test_search_mentor_by_skill_found(self):
        """TC1: Tim kiem mentor theo tu khoa 'Python' -> Tim thay ket qua."""
        # 1. Arrange
        keyword = "Python"

        # 2. Act
        results = self.manager.search_mentor(keyword)

        # 3. Assert
        self.assertGreater(len(results), 0, "Phai tim thay it nhat 1 mentor co ky nang Python")
        # Kiem tra tat ca ket qua deu chua tu khoa Python
        for mentor in results:
            self.assertIn("Python", mentor["skill"], "Ky nang cua mentor phai chua tu khoa Python")

    # ===== TEST CASE 2: Tim kiem mentor khong tim thay =====
    def test_search_mentor_not_found(self):
        """TC2: Tim kiem mentor theo tu khoa khong co -> Tra ve danh sach rong."""
        # 1. Arrange
        keyword = "Blockchain"

        # 2. Act
        results = self.manager.search_mentor(keyword)

        # 3. Assert
        self.assertEqual(len(results), 0, "Khong duoc co mentor nao co ky nang 'Blockchain'")

    # ===== TEST CASE 3: Dat lich hen thanh cong =====
    def test_book_appointment_success(self):
        """TC3: Dat lich hen giua Mentee va Mentor -> Tao thanh cong cuoc hen."""
        # 1. Arrange
        mentee = "Tran Duc Duy"
        mentor = "Nguyen Van A"
        date = "20/11/2026"
        time = "14:00"

        # 2. Act
        appointment = self.manager.book_appointment(mentee, mentor, date, time)

        # 3. Assert
        self.assertIsNotNone(appointment, "Cuoc hen phai duoc tao thanh cong")
        self.assertEqual(appointment["mentee"], mentee, "Ten mentee phai khop")
        self.assertEqual(appointment["status"], "Đã xác nhận", "Trang thai phai la 'Da xac nhan'")

    # ===== TEST CASE 4: Danh gia mentor voi so sao khong hop le =====
    def test_session_feedback_invalid_rating_fails(self):
        """TC4: Danh gia mentor voi so sao = 0 (ngoai pham vi 1-5) -> That bai."""
        # 1. Arrange
        invalid_rating = 0

        # 2. Act
        result = self.manager.session_feedback("APPT001", "Nguyen Van A", invalid_rating)

        # 3. Assert
        self.assertFalse(result, "Danh gia voi so sao ngoai pham vi 1-5 phai that bai")


if __name__ == '__main__':
    unittest.main()
