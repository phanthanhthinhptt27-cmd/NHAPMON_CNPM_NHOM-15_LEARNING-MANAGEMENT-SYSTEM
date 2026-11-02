"""Demo độc lập phân hệ Tài liệu & Bài tập (Lê Quân Bảo)."""
from .document_management import DocumentManager

def run_documents_demo():
    print("=" * 70)
    print("DEMO PHÂN HỆ: TÀI LIỆU & BÀI TẬP")
    print("Người thực hiện: Lê Quân Bảo - MSSV: 25S1020013")
    print("=" * 70)

    dm = DocumentManager()

    # 1. Tải lên tài liệu học tập
    print("\n[1] GIẢNG VIÊN TẢI TÀI LIỆU HỌC TẬP")
    dm.upload_document("C01", "Slide Chương 1: Giới thiệu Git & GitHub", "chuong1_git.pdf", "PDF")
    dm.upload_document("C01", "Hướng dẫn thực hành Sprint 0", "hdth_sprint0.docx", "Word")
    dm.display_documents()

    # 2. Sinh viên nộp bài tập
    print("\n[2] SINH VIÊN NỘP BÀI TẬP")
    sub1 = dm.submit_assignment("BT01_Gitflow", "25S1020023", "Trần Đức Duy", "bai_lam_duy.zip")
    sub2 = dm.submit_assignment("BT01_Gitflow", "25S1020013", "Lê Quân Bảo", "bai_lam_bao.zip")

    # 3. Giảng viên chấm điểm
    print("\n[3] CHẤM ĐIỂM BÀI NỘP")
    dm.grade_assignment(sub1["id"], 10, "Làm bài rất tốt, Gitflow chuẩn chỉ!")
    dm.grade_assignment(sub2["id"], 9.5, "Hoàn thành tốt các yêu cầu.")

    dm.display_submissions()

if __name__ == "__main__":
    run_documents_demo()
