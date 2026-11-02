"""
Phân hệ Tài liệu & Bài tập
Phụ trách: Lê Quân Bảo - MSSV: 25S1020013
Bao gồm:
- feature/document-upload : Tải tài liệu học tập (PDF, Slide, Tài liệu)
- feature/assignment-submission : Nộp bài tập và xem điểm số
"""

class DocumentManager:
    def __init__(self):
        self.documents = []
        self.submissions = []

    def upload_document(self, course_id, title, file_name, file_type="PDF", uploader="TS. Trần Văn Long"):
        """Tải lên tài liệu học tập mới."""
        doc = {
            "id": f"DOC{len(self.documents) + 1:03d}",
            "course_id": course_id,
            "title": title,
            "file_name": file_name,
            "file_type": file_type,
            "uploader": uploader
        }
        self.documents.append(doc)
        print(f"Thành công: Đã tải lên tài liệu '{title}' ({file_name}) cho môn {course_id}.")
        return doc

    def submit_assignment(self, assignment_id, student_id, student_name, submission_file):
        """Sinh viên nộp bài tập."""
        sub = {
            "id": f"SUB{len(self.submissions) + 1:03d}",
            "assignment_id": assignment_id,
            "student_id": student_id,
            "student_name": student_name,
            "submission_file": submission_file,
            "score": None,
            "status": "Đã nộp (Chờ chấm)"
        }
        self.submissions.append(sub)
        print(f"Thành công: Sinh viên {student_name} ({student_id}) đã nộp bài '{assignment_id}'.")
        return sub

    def grade_assignment(self, submission_id, score, feedback=""):
        """Giảng viên chấm điểm bài tập."""
        for sub in self.submissions:
            if sub["id"] == submission_id:
                sub["score"] = score
                sub["feedback"] = feedback
                sub["status"] = "Đã chấm điểm"
                print(f"Thành công: Đã chấm điểm [{score}/10] cho bài nộp {submission_id} của {sub['student_name']}.")
                return True
        print(f"Lỗi: Không tìm thấy bài nộp có mã {submission_id}.")
        return False

    def display_documents(self):
        """Hiển thị danh sách tài liệu môn học."""
        if not self.documents:
            print("Chưa có tài liệu nào được tải lên.")
            return
        print("\n=== DANH SÁCH TÀI LIỆU HỌC TẬP ===")
        for idx, doc in enumerate(self.documents, start=1):
            print(f"{idx}. [{doc['file_type']}] {doc['title']} | File: {doc['file_name']} | Người đăng: {doc['uploader']}")

    def display_submissions(self):
        """Hiển thị danh sách bài nộp và điểm số."""
        if not self.submissions:
            print("Chưa có bài nộp nào.")
            return
        print("\n=== DANH SÁCH BÀI NỘP VÀ ĐIỂM SỐ ===")
        for idx, sub in enumerate(self.submissions, start=1):
            score_str = f"{sub['score']}/10" if sub['score'] is not None else "Chưa chấm"
            print(f"{idx}. [{sub['status']}] SV: {sub['student_name']} ({sub['student_id']}) | Bài: {sub['assignment_id']} | Điểm: {score_str}")
