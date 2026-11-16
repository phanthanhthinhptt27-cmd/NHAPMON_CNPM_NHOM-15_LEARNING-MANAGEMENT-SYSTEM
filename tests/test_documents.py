"""
Unit Test - Phan he Tai lieu & Bai tap
Thanh vien: Le Quan Bao - MSSV: 25S1020013
Ap dung cau truc AAA (Arrange - Act - Assert)
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.documents.document_management import DocumentManager


class TestDocumentManagement(unittest.TestCase):
    """Test module tai lieu va bai tap - Le Quan Bao."""

    def setUp(self):
        """Khoi tao DocumentManager truoc moi test case."""
        self.manager = DocumentManager()

    # ===== TEST CASE 1: Tai len tai lieu thanh cong =====
    def test_upload_document_success(self):
        """TC1: Tai len tai lieu hoc tap moi -> Thanh cong."""
        # 1. Arrange
        course_id = "CS101"
        title = "Slide Chuong 4 - Phat trien Phan mem"
        file_name = "Chapter4_Development.pdf"

        # 2. Act
        doc = self.manager.upload_document(course_id, title, file_name)

        # 3. Assert
        self.assertIsNotNone(doc, "Tai lieu phai duoc tao thanh cong")
        self.assertEqual(doc["title"], title, "Ten tai lieu phai khop")
        self.assertEqual(len(self.manager.documents), 1, "Danh sach tai lieu phai co 1 phan tu")

    # ===== TEST CASE 2: Nop bai tap thanh cong =====
    def test_submit_assignment_success(self):
        """TC2: Sinh vien nop bai tap -> Trang thai la 'Da nop (Cho cham)'."""
        # 1. Arrange
        assignment_id = "BT01"
        student_id = "25S1020023"
        student_name = "Tran Duc Duy"
        submission_file = "BaiTap1_TranDucDuy.zip"

        # 2. Act
        sub = self.manager.submit_assignment(assignment_id, student_id, student_name, submission_file)

        # 3. Assert
        self.assertIsNotNone(sub, "Bai nop phai duoc tao thanh cong")
        self.assertEqual(sub["status"], "Đã nộp (Chờ chấm)", "Trang thai phai la 'Da nop (Cho cham)'")
        self.assertIsNone(sub["score"], "Diem so ban dau phai la None (chua cham)")

    # ===== TEST CASE 3: Cham diem bai tap thanh cong =====
    def test_grade_assignment_success(self):
        """TC3: Giang vien cham diem bai nop -> Diem so duoc cap nhat dung."""
        # 1. Arrange
        self.manager.submit_assignment("BT01", "25S1020023", "Tran Duc Duy", "BaiTap1.zip")
        submission_id = "SUB001"
        score = 8.5

        # 2. Act
        result = self.manager.grade_assignment(submission_id, score, "Bai lam tot")

        # 3. Assert
        self.assertTrue(result, "Cham diem phai thanh cong")
        graded_sub = self.manager.submissions[0]
        self.assertEqual(graded_sub["score"], 8.5, "Diem so phai la 8.5")
        self.assertEqual(graded_sub["status"], "Đã chấm điểm", "Trang thai phai chuyen thanh 'Da cham diem'")

    # ===== TEST CASE 4: Cham diem bai nop khong ton tai =====
    def test_grade_assignment_not_found_fails(self):
        """TC4: Cham diem bai nop khong ton tai trong he thong -> That bai."""
        # 1. Arrange
        fake_submission_id = "SUB_KHONG_TON_TAI"

        # 2. Act
        result = self.manager.grade_assignment(fake_submission_id, 10)

        # 3. Assert
        self.assertFalse(result, "Cham diem bai nop khong ton tai phai that bai")


if __name__ == '__main__':
    unittest.main()
