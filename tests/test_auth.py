"""
Unit Test - Phan he Quan ly Tai khoan & Phan quyen
Thanh vien: Phan Thanh Thinh (Scrum Master)
Ap dung cau truc AAA (Arrange - Act - Assert)
"""
import unittest
import sys
import os

# Them duong dan goc cua du an vao PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.auth.user_auth import UserManager


class TestUserAuthentication(unittest.TestCase):
    """Test module xac thuc nguoi dung - Phan Thanh Thinh."""

    def setUp(self):
        """Khoi tao doi tuong UserManager truoc moi test case."""
        self.manager = UserManager()

    # ===== TEST CASE 1: Dang ky tai khoan thanh cong =====
    def test_register_new_user_success(self):
        """TC1: Dang ky tai khoan moi voi thong tin hop le -> Thanh cong."""
        # 1. Arrange (Chuan bi du lieu dau vao)
        username = "sinhvien_moi"
        password = "matkhau123"
        fullname = "Nguyen Van Test"
        email = "test@lms.edu.vn"

        # 2. Act (Thuc thi ham can test)
        result = self.manager.register(username, password, fullname, email)

        # 3. Assert (Kiem chung ket qua)
        self.assertTrue(result, "Dang ky tai khoan moi phai thanh cong")
        self.assertIn(username, self.manager.users, "Tai khoan moi phai ton tai trong he thong")

    # ===== TEST CASE 2: Dang ky tai khoan bi trung ten dang nhap =====
    def test_register_duplicate_username_fails(self):
        """TC2: Dang ky tai khoan voi ten dang nhap da ton tai -> That bai."""
        # 1. Arrange
        existing_username = "admin"  # Da co san trong he thong

        # 2. Act
        result = self.manager.register(existing_username, "abc", "Test", "t@t.com")

        # 3. Assert
        self.assertFalse(result, "Dang ky trung ten dang nhap phai that bai")

    # ===== TEST CASE 3: Dang nhap thanh cong =====
    def test_login_valid_credentials_success(self):
        """TC3: Dang nhap voi thong tin chinh xac -> Thanh cong."""
        # 1. Arrange
        username = "admin"
        password = "123"

        # 2. Act
        result = self.manager.login(username, password)

        # 3. Assert
        self.assertTrue(result, "Dang nhap voi mat khau dung phai thanh cong")
        self.assertIsNotNone(self.manager.current_user, "current_user phai duoc gan sau khi dang nhap")

    # ===== TEST CASE 4: Dang nhap sai mat khau =====
    def test_login_wrong_password_fails(self):
        """TC4: Dang nhap voi mat khau sai -> That bai."""
        # 1. Arrange
        username = "admin"
        wrong_password = "sai_mat_khau"

        # 2. Act
        result = self.manager.login(username, wrong_password)

        # 3. Assert
        self.assertFalse(result, "Dang nhap voi mat khau sai phai that bai")


if __name__ == '__main__':
    unittest.main()
