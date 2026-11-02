
lê Quân Bảo 25S1020013







def demo_course_management():
    print("=" * 60)
    print("DEMO TINH NANG 1: QU?N LY KHOA H?C / MON H?C (feature/course-management)")
    print("Ngu?i th?c hi?n: Tr?n D?c Duy (MSSV: 25S1020023)")
    print("=" * 60)

    cm = CourseManager()

    # 1. T?o khóa h?c m?i
    cm.add_course("C01", "Nh?p môn Công ngh? Ph?n m?m", "TIN3142", 3, "Khóa h?c n?n t?ng v? quy trình ph?n m?m")
    cm.add_course("C02", "Co s? d? li?u", "TIN3022", 3, "Thi?t k? và qu?n tr? CSDL quan h?")
    cm.add_course("C03", "L?p trình Web nâng cao", "TIN3112", 4, "Xây d?ng ?ng d?ng web v?i Framework hi?n d?i")

    # 2. Hi?n th? danh sách khóa h?c
    cm.display_courses()

    # 3. Ch?nh s?a khóa h?c
    print("\n--- C?p nh?t thông tin khóa h?c C01 ---")
    cm.update_course("C01", name="Nh?p môn Công ngh? Ph?n m?m (Th?c hành Git)", credits=4)

    # 4. Xóa khóa h?c
    print("\n--- Xóa khóa h?c C03 ---")
    cm.delete_course("C03")

    # 5. Hi?n th? l?i danh sách sau khi s?a/xóa
    cm.display_courses()


if __name__ == "__main__":
    demo_course_management()
