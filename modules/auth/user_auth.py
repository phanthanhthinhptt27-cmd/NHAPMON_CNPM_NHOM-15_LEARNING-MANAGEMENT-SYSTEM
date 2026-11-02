"""
Phân hệ Quản lý Tài khoản & Phân quyền
Phụ trách: Phan Thanh Thịnh (Scrum Master)
Bao gồm:
- feature/user-authentication : Đăng ký, đăng nhập, đổi mật khẩu
- feature/user-profile : Xem và cập nhật thông tin cá nhân
- feature/role-permission : Phân quyền vai trò (Admin, Giảng viên, Sinh viên)
"""

class UserManager:
    def __init__(self):
        self.users = {
            "admin": {
                "username": "admin",
                "password": "123",
                "role": "Admin",
                "fullname": "Quản trị viên Hệ thống",
                "email": "admin@lms.edu.vn",
                "phone": "0901234567"
            },
            "thinhpt": {
                "username": "thinhpt",
                "password": "123",
                "role": "Giảng viên",
                "fullname": "ThS. Phan Thanh Thịnh",
                "email": "thinhpt@lms.edu.vn",
                "phone": "0912345678"
            },
            "duytd": {
                "username": "duytd",
                "password": "123",
                "role": "Sinh viên",
                "fullname": "Trần Đức Duy",
                "email": "duytd@lms.edu.vn",
                "phone": "0987654321"
            }
        }
        self.current_user = None

    def register(self, username, password, fullname, email, role="Sinh viên"):
        """Đăng ký tài khoản mới."""
        if username in self.users:
            print(f"Lỗi: Tên đăng nhập '{username}' đã tồn tại!")
            return False
        self.users[username] = {
            "username": username,
            "password": password,
            "role": role,
            "fullname": fullname,
            "email": email,
            "phone": ""
        }
        print(f"Thành công: Đăng ký tài khoản '{username}' với vai trò [{role}] thành công.")
        return True

    def login(self, username, password):
        """Đăng nhập hệ thống."""
        if username in self.users and self.users[username]["password"] == password:
            self.current_user = self.users[username]
            print(f"Thành công: Đăng nhập thành công! Xin chào {self.current_user['fullname']} ({self.current_user['role']}).")
            return True
        print("Lỗi: Tên đăng nhập hoặc mật khẩu không chính xác!")
        return False

    def change_password(self, username, old_password, new_password):
        """Đổi mật khẩu tài khoản."""
        if username in self.users and self.users[username]["password"] == old_password:
            self.users[username]["password"] = new_password
            print(f"Thành công: Đã đổi mật khẩu cho tài khoản '{username}'.")
            return True
        print("Lỗi: Mật khẩu cũ không chính xác!")
        return False

    def update_profile(self, username, fullname=None, email=None, phone=None):
        """Cập nhật hồ sơ cá nhân."""
        if username not in self.users:
            print(f"Lỗi: Không tìm thấy tài khoản '{username}'.")
            return False
        if fullname:
            self.users[username]["fullname"] = fullname
        if email:
            self.users[username]["email"] = email
        if phone:
            self.users[username]["phone"] = phone
        print(f"Thành công: Đã cập nhật hồ sơ cá nhân cho '{username}'.")
        return True

    def assign_role(self, admin_username, target_username, new_role):
        """Admin phân quyền vai trò cho người dùng."""
        if admin_username not in self.users or self.users[admin_username]["role"] != "Admin":
            print(f"Lỗi: Người dùng '{admin_username}' không có quyền Admin để phân quyền!")
            return False
        if target_username not in self.users:
            print(f"Lỗi: Không tìm thấy người dùng '{target_username}'.")
            return False
        self.users[target_username]["role"] = new_role
        print(f"Thành công: Admin đã phân quyền vai trò [{new_role}] cho tài khoản '{target_username}'.")
        return True

    def display_users(self):
        """Hiển thị danh sách người dùng trong hệ thống."""
        print("\n=== DANH SÁCH NGƯỜI DÙNG & VAI TRÒ ===")
        for idx, (uname, udata) in enumerate(self.users.items(), start=1):
            print(f"{idx}. {udata['fullname']} (@{uname}) | Vai trò: [{udata['role']}] | Email: {udata['email']}")
