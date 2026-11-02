"""
Chương trình chính LMS (Learning Management System)
Nhóm 15 - Nhập môn Công nghệ Phần mềm
Thành viên phụ trách Quản lý Lớp học & Giảng dạy: Trần Đức Duy - MSSV: 25S1020023
"""
from course_management import CourseManager


def demo_course_management():
    print("=" * 60)
    print("DEMO TÍNH NĂNG 1: QUẢN LÝ KHÓA HỌC / MÔN HỌC (feature/course-management)")
    print("Người thực hiện: Trần Đức Duy (MSSV: 25S1020023)")
    print("=" * 60)

    cm = CourseManager()

    # 1. Tạo khóa học mới
    cm.add_course("C01", "Nhập môn Công nghệ Phần mềm", "TIN3142", 3, "Khóa học nền tảng về quy trình phần mềm")
    cm.add_course("C02", "Cơ sở dữ liệu", "TIN3022", 3, "Thiết kế và quản trị CSDL quan hệ")
    cm.add_course("C03", "Lập trình Web nâng cao", "TIN3112", 4, "Xây dựng ứng dụng web với Framework hiện đại")

    # 2. Hiển thị danh sách khóa học
    cm.display_courses()

    # 3. Chỉnh sửa khóa học
    print("\n--- Cập nhật thông tin khóa học C01 ---")
    cm.update_course("C01", name="Nhập môn Công nghệ Phần mềm (Thực hành Git)", credits=4)

    # 4. Xóa khóa học
    print("\n--- Xóa khóa học C03 ---")
    cm.delete_course("C03")

    # 5. Hiển thị lại danh sách sau khi sửa/xóa
    cm.display_courses()


if __name__ == "__main__":
    demo_course_management()
