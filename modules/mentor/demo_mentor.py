"""Demo độc lập phân hệ Mentor - Mentee (Phan Văn Hảo)."""
from .mentor_management import MentorManager

def run_mentor_demo():
    print("=" * 70)
    print("DEMO PHÂN HỆ: KẾT NỐI MENTOR - MENTEE")
    print("Người thực hiện: Phan Văn Hảo")
    print("=" * 70)

    mm = MentorManager()

    # 1. Tìm kiếm mentor
    print("\n[1] TÌM KIẾM MENTOR (Từ khóa: 'Python')")
    found = mm.search_mentor("Python")
    mm.display_mentors(found)

    # 2. Đặt lịch hẹn
    print("\n[2] ĐẶT LỊCH HẸN TƯ VẤN")
    appt = mm.book_appointment("Trần Đức Duy", "Lê Văn C", "2026-11-05", "14:00 - 15:30", "Tư vấn lộ trình học AI")

    # 3. Đánh giá buổi hẹn
    print("\n[3] ĐÁNH GIÁ VÀ PHẢN HỒI BUỔI HẸN")
    mm.session_feedback(appt["id"], "Lê Văn C", 5, "Mentor hướng dẫn rất nhiệt tình và dễ hiểu!")

if __name__ == "__main__":
    run_mentor_demo()
