"""Demo độc lập phân hệ Quản lý Lớp học & Giảng dạy (Trần Đức Duy)."""
from .course_management import CourseManager
from .schedule_assignment import ScheduleManager
from .attendance_tracking import AttendanceManager


def run_lms_demo():
    print("=" * 70)
    print("DEMO PHÂN HỆ: QUẢN LÝ LỚP HỌC & GIẢNG DẠY (LMS)")
    print("Người thực hiện: Trần Đức Duy - MSSV: 25S1020023")
    print("=" * 70)

    # 1. Quản lý khóa học
    print("\n[1] KHỞI TẠO VÀ QUẢN LÝ KHÓA HỌC")
    cm = CourseManager()
    cm.add_course("C01", "Nhập môn Công nghệ Phần mềm", "TIN3142", 3, "Khóa học quy trình phần mềm & Scrum")
    cm.add_course("C02", "Cơ sở dữ liệu", "TIN3022", 3, "Thiết kế và quản trị CSDL quan hệ")
    cm.display_courses()

    # 2. Phân công giảng viên & lịch học
    print("\n[2] PHÂN CÔNG GIẢNG VIÊN VÀ XẾP LỊCH HỌC")
    sm = ScheduleManager()
    sm.add_instructor("GV01", "TS. Trần Văn Long", "tvlong@hueuni.edu.vn", "Khoa Tin học")
    sm.add_instructor("GV02", "ThS. Phan Thanh Thịnh", "ptthinh@hueuni.edu.vn", "Khoa Tin học")

    sm.assign_schedule("SCH01", "C01", "GV01", "Thứ 2", "07:30 - 09:30", "Phòng A201", course_manager=cm)
    sm.assign_schedule("SCH02", "C02", "GV02", "Thứ 4", "13:30 - 15:30", "Phòng Lab 3", course_manager=cm)
    sm.display_schedules(course_manager=cm)

    # 3. Điểm danh sinh viên
    print("\n[3] ĐĂNG KÝ SINH VIÊN VÀ ĐIỂM DANH BUỔI HỌC")
    am = AttendanceManager()
    am.register_student("25S1020023", "Trần Đức Duy", "duy.tran@student.edu.vn")
    am.register_student("25S1020001", "Nguyễn Văn Bảo", "bao.nguyen@student.edu.vn")
    am.register_student("25S1020002", "Lê Thị Thảo", "thao.le@student.edu.vn")

    am.mark_attendance("SCH01", "2026-11-02", "25S1020023", status="Có mặt", schedule_manager=sm)
    am.mark_attendance("SCH01", "2026-11-02", "25S1020001", status="Vắng mặt", note="Không phép", schedule_manager=sm)
    am.mark_attendance("SCH01", "2026-11-02", "25S1020002", status="Có mặt", schedule_manager=sm)

    am.display_attendance_report("SCH01", session_date="2026-11-02", schedule_manager=sm, course_manager=cm)


if __name__ == "__main__":
    run_lms_demo()
