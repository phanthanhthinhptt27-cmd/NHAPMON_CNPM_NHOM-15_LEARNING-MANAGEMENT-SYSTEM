"""
Chương trình chính LMS (Learning Management System)
Nhóm 15 - Nhập môn Công nghệ Phần mềm
Thành viên phụ trách Quản lý Lớp học & Giảng dạy: Trần Đức Duy - MSSV: 25S1020023
"""
from course_management import CourseManager
from schedule_assignment import ScheduleManager


def main():
    print("=" * 65)
    print("HỆ THỐNG LMS - PHÂN HỆ QUẢN LÝ LỚP HỌC & GIẢNG DẠY")
    print("Người thực hiện: Trần Đức Duy (MSSV: 25S1020023)")
    print("=" * 65)

    # 1. Quản lý khóa học (feature/course-management)
    cm = CourseManager()
    print("\n--- 1. KHỞI TẠO VÀ QUẢN LÝ KHÓA HỌC ---")
    cm.add_course("C01", "Nhập môn Công nghệ Phần mềm", "TIN3142", 3, "Khóa học nền tảng về quy trình phần mềm")
    cm.add_course("C02", "Cơ sở dữ liệu", "TIN3022", 3, "Thiết kế và quản trị CSDL quan hệ")
    cm.display_courses()

    # 2. Phân công giảng viên & Xếp lịch học (feature/schedule-assignment)
    sm = ScheduleManager()
    print("\n--- 2. THÊM GIẢNG VIÊN VÀ PHÂN CÔNG LỊCH HỌC ---")
    sm.add_instructor("GV01", "TS. Trần Văn Long", "tvlong@hueuni.edu.vn", "Khoa Tin học")
    sm.add_instructor("GV02", "ThS. Nguyễn Văn A", "nva@hueuni.edu.vn", "Khoa Tin học")

    sm.assign_schedule("SCH01", "C01", "GV01", "Thứ 2", "07:30 - 09:30", "Phòng A201", course_manager=cm)
    sm.assign_schedule("SCH02", "C02", "GV02", "Thứ 4", "13:30 - 15:30", "Phòng Lab 3", course_manager=cm)

    sm.display_schedules(course_manager=cm)


if __name__ == "__main__":
    main()
