"""
Module Thư viện & Phạt mượn sách quá hạn (Library Fine Calculator)
Bài tập thực hành Hoạt động 3 - Chương 4: Nhập môn Công nghệ Phần mềm
Giảng viên: TS. Trần Văn Long
Quy tắc tính phạt:
- 5.000đ / ngày quá hạn.
- Nếu quá hạn > 10 ngày, phạt thêm 20% (nhân 1.2).
- Nếu số ngày <= 0, tiền phạt = 0đ.
"""

class FineCalculator:
    def calculate(self, days_overdue: int) -> float:
        """
        Tính số tiền phạt mượn sách quá hạn.
        :param days_overdue: Số ngày quá hạn (int)
        :return: Số tiền phạt theo VNĐ (float)
        """
        if days_overdue <= 0:
            return 0.0
        
        fine = float(days_overdue * 5000)
        if days_overdue > 10:
            fine = fine * 1.2
            
        return fine
