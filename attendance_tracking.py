"""
Module Điểm danh Sinh viên (Attendance Tracking)
Phụ trách: Trần Đức Duy - MSSV: 25S1020023
Nhánh: feature/attendance-tracking
"""


class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"SV: {self.name} ({self.student_id})"


class AttendanceRecord:
    def __init__(self, record_id, schedule_id, session_date, student_id, status="Có mặt", note=""):
        self.record_id = record_id
        self.schedule_id = schedule_id
        self.session_date = session_date    # Ví dụ: "2026-11-02"
        self.student_id = student_id
        self.status = status                # "Có mặt", "Vắng mặt", "Có phép"
        self.note = note

    def __str__(self):
        return f"[{self.session_date}] Lớp {self.schedule_id} | SV {self.student_id}: {self.status} ({self.note})"


class AttendanceManager:
    def __init__(self):
        self.students = {}
        self.records = []
        self._record_counter = 1

    def register_student(self, student_id, name, email):
        """Đăng ký sinh viên vào danh sách lớp/hệ thống."""
        if student_id in self.students:
            print(f"Lỗi: Sinh viên với mã '{student_id}' đã tồn tại!")
            return False

        student = Student(student_id, name, email)
        self.students[student_id] = student
        print(f"Thành công: Đã đăng ký sinh viên '{name}' ({student_id}).")
        return True

    def get_student(self, student_id):
        """Lấy thông tin sinh viên theo mã."""
        return self.students.get(student_id)

    def mark_attendance(self, schedule_id, session_date, student_id, status="Có mặt", note="", schedule_manager=None):
        """Điểm danh sinh viên theo buổi học của một lịch học."""
        if student_id not in self.students:
            print(f"Lỗi: Không tìm thấy sinh viên có mã '{student_id}'.")
            return False

        if schedule_manager and not schedule_manager.get_schedule(schedule_id):
            print(f"Lỗi: Không tìm thấy lịch học '{schedule_id}'.")
            return False

        # Kiểm tra xem đã điểm danh sinh viên này trong buổi học đó chưa
        for rec in self.records:
            if rec.schedule_id == schedule_id and rec.session_date == session_date and rec.student_id == student_id:
                rec.status = status
                rec.note = note
                print(f"Thành công: Cập nhật điểm danh cho SV '{self.students[student_id].name}' thành '{status}'.")
                return True

        record_id = f"ATT{self._record_counter:03d}"
        self._record_counter += 1
        record = AttendanceRecord(record_id, schedule_id, session_date, student_id, status, note)
        self.records.append(record)
        print(f"Thành công: Điểm danh cho SV '{self.students[student_id].name}' - Trạng thái: [{status}].")
        return True

    def get_records_by_schedule(self, schedule_id, session_date=None):
        """Lấy danh sách bản ghi điểm danh theo lịch học và ngày."""
        results = [r for r in self.records if r.schedule_id == schedule_id]
        if session_date:
            results = [r for r in results if r.session_date == session_date]
        return results

    def display_attendance_report(self, schedule_id, session_date=None, schedule_manager=None, course_manager=None):
        """Hiển thị báo cáo điểm danh chi tiết theo buổi học."""
        records = self.get_records_by_schedule(schedule_id, session_date)
        if not records:
            print(f"Không có dữ liệu điểm danh cho lịch [{schedule_id}].")
            return

        schedule_info = schedule_id
        if schedule_manager:
            sch = schedule_manager.get_schedule(schedule_id)
            if sch:
                c_name = sch.course_id
                if course_manager:
                    c = course_manager.get_course(sch.course_id)
                    if c:
                        c_name = c.name
                schedule_info = f"{c_name} - {sch.day_of_week} ({sch.session_time}) tại {sch.room}"

        print(f"\n=== BÁO CÁO ĐIỂM DANH LỚP: {schedule_info} ===")
        for idx, rec in enumerate(records, start=1):
            sv_name = self.students[rec.student_id].name if rec.student_id in self.students else rec.student_id
            status_icon = "✓" if rec.status == "Có mặt" else ("✗" if rec.status == "Vắng mặt" else "P")
            note_str = f" ({rec.note})" if rec.note else ""
            print(f"{idx}. [{status_icon}] {sv_name} ({rec.student_id}) - Ngày: {rec.session_date} | Trạng thái: {rec.status}{note_str}")
