"""
CHƯƠNG TRÌNH ĐIỀU KHIỂN CHÍNH (MAIN APPLICATION ENTRY POINT)
Học phần: Nhập môn Công nghệ Phần mềm
Đồ án: LEARNING MANAGEMENT SYSTEM (LMS) & MENTOR - MENTEE
Nhóm: 15

Danh sách thành viên & phân công:
1. Phan Thanh Thịnh (Scrum Master) - Quản lý Tài khoản & Phân quyền
2. Trần Đức Duy (MSSV: 25S1020023) - Quản lý Lớp học & Giảng dạy (LMS)
3. Phan Văn Hảo - Kết nối Mentor - Mentee
4. Lê Quân Bảo (MSSV: 25S1020013) - Tài liệu & Bài tập
"""
import sys
import os

from modules.auth import run_auth_demo
from modules.lms import run_lms_demo
from modules.mentor import run_mentor_demo
from modules.documents import run_documents_demo


def run_all_demos():
    """Chạy toàn bộ demo 4 phân hệ liên hoàn."""
    print("\n" + "=" * 80)
    print("   BẮT ĐẦU CHẠY KIỂM THỬ TOÀN DIỆN CẢ 4 PHÂN HỆ HỆ THỐNG LMS (NHÓM 15)")
    print("=" * 80)
    
    print("\n>>> [1/4] KIỂM THỬ PHÂN HỆ TÀI KHOẢN & PHÂN QUYỀN...")
    run_auth_demo()

    print("\n>>> [2/4] KIỂM THỬ PHÂN HỆ QUẢN LÝ LỚP HỌC & GIẢNG DẠY (LMS)...")
    run_lms_demo()

    print("\n>>> [3/4] KIỂM THỬ PHÂN HỆ KẾT NỐI MENTOR - MENTEE...")
    run_mentor_demo()

    print("\n>>> [4/4] KIỂM THỬ PHÂN HỆ TÀI LIỆU & BÀI TẬP...")
    run_documents_demo()

    print("\n" + "=" * 80)
    print("   ✓ HOÀN THÀNH KIỂM THỬ TẤT CẢ 4 PHÂN HỆ - HỆ THỐNG HOẠT ĐỘNG HOÀN HẢO!")
    print("=" * 80)


def show_menu():
    while True:
        print("\n" + "=" * 70)
        print("   HỆ THỐNG QUẢN LÝ HỌC TẬP & KẾT NỐI MENTOR (LMS - NHÓM 15)")
        print("=" * 70)
        print("  1. Phân hệ 1: Quản lý Tài khoản & Phân quyền (Phan Thanh Thịnh)")
        print("  2. Phân hệ 2: Quản lý Lớp học & Giảng dạy (Trần Đức Duy)")
        print("  3. Phân hệ 3: Kết nối Mentor - Mentee (Phan Văn Hảo)")
        print("  4. Phân hệ 4: Tài liệu & Bài tập (Lê Quân Bảo)")
        print("  5. Chạy kiểm thử toàn bộ hệ thống (End-to-End Test)")
        print("  0. Thoát chương trình")
        print("-" * 70)

        choice = input("Mời bạn chọn chức năng (0-5): ").strip()

        if choice == "1":
            run_auth_demo()
        elif choice == "2":
            run_lms_demo()
        elif choice == "3":
            run_mentor_demo()
        elif choice == "4":
            run_documents_demo()
        elif choice == "5":
            run_all_demos()
        elif choice == "0":
            print("\nCảm ơn thầy và các bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 0 đến 5.")


if __name__ == "__main__":
    # Nếu chạy trực tiếp kèm tham số --all thì chạy toàn bộ demo tự động
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        run_all_demos()
    else:
        # Mặc định chạy toàn bộ demo một lần rồi mở menu để thầy dễ chấm
        run_all_demos()
