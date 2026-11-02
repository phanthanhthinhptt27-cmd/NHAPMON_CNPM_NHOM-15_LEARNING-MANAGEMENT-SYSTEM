"""
Module Quản lý Khóa học & Môn học (Course Management)
Phụ trách: Trần Đức Duy - MSSV: 25S1020023
Nhánh: feature/course-management
"""

class Course:
    def __init__(self, course_id, name, code, credits=3, description=""):
        self.course_id = course_id
        self.name = name
        self.code = code
        self.credits = credits
        self.description = description

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits,
            "description": self.description,
        }

    def __str__(self):
        return f"[{self.code}] {self.name} ({self.credits} tín chỉ) - {self.description}"


class CourseManager:
    def __init__(self):
        self.courses = {}

    def add_course(self, course_id, name, code, credits=3, description=""):
        """Tạo khóa học/môn học mới."""
        if course_id in self.courses:
            print(f"Lỗi: Mã định danh khóa học '{course_id}' đã tồn tại!")
            return False
        
        course = Course(course_id, name, code, credits, description)
        self.courses[course_id] = course
        print(f"Thành công: Đã thêm khóa học '{name}' ({code}).")
        return True

    def get_course(self, course_id):
        """Lấy thông tin khóa học theo ID."""
        return self.courses.get(course_id)

    def update_course(self, course_id, name=None, code=None, credits=None, description=None):
        """Chỉnh sửa thông tin khóa học."""
        course = self.get_course(course_id)
        if not course:
            print(f"Lỗi: Không tìm thấy khóa học với mã '{course_id}'.")
            return False

        if name is not None:
            course.name = name
        if code is not None:
            course.code = code
        if credits is not None:
            course.credits = credits
        if description is not None:
            course.description = description

        print(f"Thành công: Đã cập nhật khóa học '{course.code}'.")
        return True

    def delete_course(self, course_id):
        """Xóa một khóa học khỏi danh sách."""
        if course_id in self.courses:
            removed = self.courses.pop(course_id)
            print(f"Thành công: Đã xóa khóa học '{removed.name}' ({removed.code}).")
            return True
        print(f"Lỗi: Không tìm thấy khóa học với mã '{course_id}' để xóa.")
        return False

    def list_courses(self):
        """Lấy danh sách tất cả khóa học."""
        return list(self.courses.values())

    def display_courses(self):
        """Hiển thị danh sách khóa học có đánh số thứ tự."""
        courses = self.list_courses()
        if not courses:
            print("Danh sách khóa học hiện đang trống.")
            return

        print("\n=== DANH SÁCH KHÓA HỌC / MÔN HỌC ===")
        for idx, course in enumerate(courses, start=1):
            print(f"{idx}. Mã môn: {course.code} | Tên: {course.name} | Tín chỉ: {course.credits} | ID: {course.course_id}")
