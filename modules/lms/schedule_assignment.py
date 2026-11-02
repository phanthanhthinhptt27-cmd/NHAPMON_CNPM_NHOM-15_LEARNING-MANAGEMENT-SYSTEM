"""
Module Phân công Giảng viên & Xếp lịch học (Schedule Assignment)
Phụ trách: Trần Đức Duy - MSSV: 25S1020023
Nhánh: feature/schedule-assignment
"""


class Instructor:
    def __init__(self, instructor_id, name, email, department="Công nghệ Thông tin"):
        self.instructor_id = instructor_id
        self.name = name
        self.email = email
        self.department = department

    def __str__(self):
        return f"GV: {self.name} ({self.instructor_id}) - Khoa: {self.department}"


class Schedule:
    def __init__(self, schedule_id, course_id, instructor_id, day_of_week, session_time, room):
        self.schedule_id = schedule_id
        self.course_id = course_id
        self.instructor_id = instructor_id
        self.day_of_week = day_of_week        # Ví dụ: "Thứ 2", "Thứ 4"
        self.session_time = session_time      # Ví dụ: "07:30 - 09:30"
        self.room = room                      # Ví dụ: "Phòng A201"

    def __str__(self):
        return f"Lịch [{self.schedule_id}]: Khóa {self.course_id} - GV {self.instructor_id} | {self.day_of_week} ({self.session_time}) tại {self.room}"


class ScheduleManager:
    def __init__(self):
        self.instructors = {}
        self.schedules = {}

    def add_instructor(self, instructor_id, name, email, department="Khoa Tin học"):
        """Thêm giảng viên vào hệ thống."""
        if instructor_id in self.instructors:
            print(f"Lỗi: Mã giảng viên '{instructor_id}' đã tồn tại!")
            return False
        
        instructor = Instructor(instructor_id, name, email, department)
        self.instructors[instructor_id] = instructor
        print(f"Thành công: Đã thêm giảng viên '{name}' ({instructor_id}).")
        return True

    def get_instructor(self, instructor_id):
        """Lấy thông tin giảng viên theo ID."""
        return self.instructors.get(instructor_id)

    def list_instructors(self):
        """Lấy danh sách tất cả giảng viên."""
        return list(self.instructors.values())

    def assign_schedule(self, schedule_id, course_id, instructor_id, day_of_week, session_time, room, course_manager=None):
        """Phân công giảng viên và xếp lịch học cho môn học."""
        if schedule_id in self.schedules:
            print(f"Lỗi: Mã lịch học '{schedule_id}' đã tồn tại!")
            return False

        if instructor_id not in self.instructors:
            print(f"Lỗi: Không tìm thấy giảng viên với mã '{instructor_id}'.")
            return False

        if course_manager and not course_manager.get_course(course_id):
            print(f"Lỗi: Không tìm thấy khóa học với mã '{course_id}'.")
            return False

        schedule = Schedule(schedule_id, course_id, instructor_id, day_of_week, session_time, room)
        self.schedules[schedule_id] = schedule
        print(f"Thành công: Đã xếp lịch [{schedule_id}] cho môn {course_id} - GV phụ trách: {self.instructors[instructor_id].name}.")
        return True

    def get_schedule(self, schedule_id):
        """Lấy thông tin một lịch học."""
        return self.schedules.get(schedule_id)

    def list_schedules(self):
        """Lấy danh sách tất cả lịch học."""
        return list(self.schedules.values())

    def display_schedules(self, course_manager=None):
        """Hiển thị danh sách lịch học và phân công giảng dạy chi tiết."""
        schedules = self.list_schedules()
        if not schedules:
            print("Chưa có lịch học nào được xếp.")
            return

        print("\n=== BẢNG PHÂN CÔNG GIẢNG VIÊN VÀ LỊCH HỌC ===")
        for idx, s in enumerate(schedules, start=1):
            course_name = s.course_id
            if course_manager:
                c = course_manager.get_course(s.course_id)
                if c:
                    course_name = f"{c.name} ({c.code})"

            inst_name = s.instructor_id
            if s.instructor_id in self.instructors:
                inst_name = self.instructors[s.instructor_id].name

            print(f"{idx}. Mã lịch: {s.schedule_id} | Môn: {course_name} | GV: {inst_name} | Thời gian: {s.day_of_week} [{s.session_time}] | Phòng: {s.room}")
