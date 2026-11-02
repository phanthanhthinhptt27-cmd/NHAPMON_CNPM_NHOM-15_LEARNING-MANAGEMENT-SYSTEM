"""Package Phân hệ Quản lý Lớp học & Giảng dạy (LMS)."""
from .course_management import Course, CourseManager
from .schedule_assignment import Instructor, Schedule, ScheduleManager
from .attendance_tracking import Student, AttendanceRecord, AttendanceManager
from .demo_lms import run_lms_demo

__all__ = [
    "Course", "CourseManager",
    "Instructor", "Schedule", "ScheduleManager",
    "Student", "AttendanceRecord", "AttendanceManager",
    "run_lms_demo",
]
