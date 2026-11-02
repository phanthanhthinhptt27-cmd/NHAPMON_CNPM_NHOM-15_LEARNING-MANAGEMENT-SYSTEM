"""
Phân hệ Kết nối Mentor - Mentee
Phụ trách: Phan Văn Hảo
Bao gồm:
- feature/search-mentor : Tìm kiếm Mentor theo kỹ năng/chuyên môn
- feature/book-appointment : Đặt lịch hẹn tư vấn giữa Mentor và Mentee
- feature/session-feedback : Đánh giá và phản hồi sau buổi hẹn
"""

class MentorManager:
    def __init__(self):
        self.mentors = [
            {"id": "M01", "name": "Nguyễn Văn A", "skill": "Python / Django", "email": "nva@gmail.com"},
            {"id": "M02", "name": "Trần Văn B", "skill": "Java / Spring Boot", "email": "tvb@gmail.com"},
            {"id": "M03", "name": "Lê Văn C", "skill": "Python / AI / Machine Learning", "email": "lvc@gmail.com"},
            {"id": "M04", "name": "Hoàng Thị D", "skill": "ReactJS / Frontend", "email": "htd@gmail.com"}
        ]
        self.appointments = []
        self.feedbacks = []

    def search_mentor(self, keyword):
        """Tìm kiếm mentor theo kỹ năng chuyên môn."""
        result = []
        for m in self.mentors:
            if keyword.lower() in m["skill"].lower() or keyword.lower() in m["name"].lower():
                result.append(m)
        return result

    def book_appointment(self, mentee_name, mentor_name, date, time, note=""):
        """Đặt lịch hẹn giữa Mentor và Mentee."""
        appt = {
            "id": f"APPT{len(self.appointments) + 1:03d}",
            "mentee": mentee_name,
            "mentor": mentor_name,
            "date": date,
            "time": time,
            "note": note,
            "status": "Đã xác nhận"
        }
        self.appointments.append(appt)
        print(f"Thành công: Đã đặt lịch hẹn [{appt['id']}] với Mentor {mentor_name} vào lúc {time} ngày {date}.")
        return appt

    def session_feedback(self, appointment_id, mentor_name, rating, comment=""):
        """Ghi nhận đánh giá sau buổi hẹn."""
        if rating < 1 or rating > 5:
            print("Lỗi: Số sao đánh giá phải từ 1 đến 5!")
            return False

        fb = {
            "appointment_id": appointment_id,
            "mentor": mentor_name,
            "rating": rating,
            "comment": comment
        }
        self.feedbacks.append(fb)
        stars = "★" * rating + "☆" * (5 - rating)
        print(f"Thành công: Đã gửi đánh giá cho Mentor {mentor_name} [{stars}] ({rating}/5 sao).")
        return True

    def display_mentors(self, mentor_list=None):
        """Hiển thị danh sách mentor."""
        items = mentor_list if mentor_list is not None else self.mentors
        if not items:
            print("Không tìm thấy Mentor nào phù hợp!")
            return
        print("\n=== DANH SÁCH MENTOR ===")
        for idx, m in enumerate(items, start=1):
            print(f"{idx}. {m['name']} - Chuyên môn: {m['skill']} | Email: {m['email']}")
