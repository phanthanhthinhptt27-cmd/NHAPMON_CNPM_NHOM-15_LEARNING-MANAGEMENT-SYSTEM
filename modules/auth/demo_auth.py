"""Demo độc lập phân hệ Tài khoản & Phân quyền (Phan Thanh Thịnh)."""
from .user_auth import UserManager

def run_auth_demo():
    print("=" * 70)
    print("DEMO PHÂN HỆ: QUẢN LÝ TÀI KHOẢN & PHÂN QUYỀN")
    print("Người thực hiện: Phan Thanh Thịnh (Scrum Master)")
    print("=" * 70)

    um = UserManager()

    # 1. Hiển thị danh sách tài khoản hiện tại
    print("\n[1] DANH SÁCH TÀI KHOẢN BAN ĐẦU")
    um.display_users()

    # 2. Đăng ký tài khoản mới
    print("\n[2] ĐĂNG KÝ TÀI KHOẢN MỚI")
    um.register("baolq", "123456", "Lê Quân Bảo", "baolq@lms.edu.vn", role="Sinh viên")

    # 3. Đăng nhập
    print("\n[3] ĐĂNG NHẬP HỆ THỐNG")
    um.login("baolq", "123456")

    # 4. Cập nhật hồ sơ cá nhân
    print("\n[4] CẬP NHẬT HỒ SƠ CÁ NHÂN")
    um.update_profile("baolq", phone="0935123456")

    # 5. Admin phân quyền vai trò
    print("\n[5] ADMIN PHÂN QUYỀN VAI TRÒ")
    um.assign_role("admin", "baolq", "Giảng viên Trợ giảng")
    um.display_users()

if __name__ == "__main__":
    run_auth_demo()
