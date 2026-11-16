# NHAPMON_CNPM_NHOM-15_LEARNING-MANAGEMENT-SYSTEM

Dự án thực hành học phần **Nhập môn Công nghệ Phần mềm** - TS. Trần Văn Long, Khoa Tin học, Trường Đại học Sư phạm, Đại học Huế.

## Tầm nhìn sản phẩm (Product Vision)
Dành cho sinh viên cần định hướng học tập và cố vấn chuyên môn, **Hệ thống Quản lý Học tập & Kết nối Mentor - Mentee (LMS)** là một nền tảng cầu nối tương tác, giúp sinh viên dễ dàng tìm kiếm cố vấn phù hợp, đặt lịch hẹn tư vấn, theo dõi lộ trình phát triển cá nhân và quản lý tiến độ học tập một cách chủ động, trực quan và hiệu quả.

---

## Danh sách thành viên & Phân công nhiệm vụ (Nhóm 15)

| STT | Họ và tên | MSSV | Tài khoản GitHub | Phân hệ phụ trách |
| :---: | :--- | :---: | :---: | :--- |
| 1 | **Phan Thanh Thịnh** *(Scrum Master)* | | `@phanthanhthinhptt27-cmd` | **Phân hệ 1:** Quản lý Tài khoản & Phân quyền |
| 2 | **Trần Đức Duy** | `25S1020023` | [`@tranduy123-hue`](https://github.com/tranduy123-hue) | **Phân hệ 2:** Quản lý Lớp học & Giảng dạy (LMS) |
| 3 | **Phan Văn Hảo** | | `@phanvanhao1103-create` | **Phân hệ 3:** Kết nối Mentor - Mentee |
| 4 | **Lê Quân Bảo** | `25S1020013` | `@lequanbaodepzai` | **Phân hệ 4:** Tài liệu & Bài tập |

---

## Kiến trúc thư mục dự án (Modular Architecture)

Dự án được tái cấu trúc theo mô hình **Module hóa** chuẩn mực của Công nghệ Phần mềm, đảm bảo tính độc lập và dễ mở rộng:

```text
NHAPMON_CNPM_NHOM-15_LEARNING-MANAGEMENT-SYSTEM/
├── README.md                      # Tài liệu tổng quan & phân công nhóm
├── .gitignore                     # Bỏ qua các tệp tạm, cache Python
├── app.py                         # File chạy chính (Menu điều khiển & Demo toàn hệ thống)
│
└── modules/                       # Thư mục chứa 4 phân hệ nghiệp vụ
    ├── __init__.py
    │
    ├── auth/                      # [Phân hệ 1] Quản lý Tài khoản & Phân quyền
    │   ├── user_auth.py           # Đăng ký, đăng nhập, đổi mật khẩu, phân quyền vai trò
    │   └── demo_auth.py           # Kịch bản kiểm thử độc lập phân hệ 1
    │
    ├── lms/                       # [Phân hệ 2] Quản lý Lớp học & Giảng dạy (Trần Đức Duy)
    │   ├── course_management.py   # Tạo, sửa, xóa và hiển thị khóa học/môn học
    │   ├── schedule_assignment.py # Phân công giảng viên và xếp lịch học
    │   ├── attendance_tracking.py # Điểm danh sinh viên theo từng buổi học
    │   └── demo_lms.py            # Kịch bản kiểm thử độc lập phân hệ 2
    │
    ├── mentor/                    # [Phân hệ 3] Kết nối Mentor - Mentee
    │   ├── mentor_management.py   # Tìm kiếm mentor, đặt lịch hẹn, đánh giá sau buổi hẹn
    │   └── demo_mentor.py         # Kịch bản kiểm thử độc lập phân hệ 3
    │
    └── documents/                 # [Phân hệ 4] Tài liệu & Bài tập
        ├── document_management.py # Tải lên tài liệu học tập, nộp bài & chấm điểm
        └── demo_documents.py      # Kịch bản kiểm thử độc lập phân hệ 4
```

---

## Hướng dẫn chạy thử nghiệm chương trình

### Cách 1: Chạy toàn bộ hệ thống từ file điều khiển chính
```bash
python app.py
```
*(Chương trình sẽ tự động chạy toàn bộ kịch bản kiểm thử liên hoàn của cả 4 phân hệ, sau đó mở Menu tương tác để người dùng tùy chọn)*.

### Cách 2: Chạy kiểm thử độc lập từng phân hệ riêng biệt
* **Phân hệ 1 (Tài khoản & Phân quyền):**
  ```bash
  python -m modules.auth.demo_auth
  ```
* **Phân hệ 2 (Quản lý Lớp học & Giảng dạy - Duy):**
  ```bash
  python -m modules.lms.demo_lms
  ```
* **Phân hệ 3 (Kết nối Mentor - Mentee):**
  ```bash
  python -m modules.mentor.demo_mentor
  ```
* **Phân hệ 4 (Tài liệu & Bài tập):**
  ```bash
  python -m modules.documents.demo_documents
  ```

---

## Chương 4: Phát triển, Tích hợp & Đảm bảo chất lượng (Sprint 1 Mini & Unit Testing)

Hệ thống kiểm thử tự động (Unit Testing) được áp dụng chặt chẽ theo cấu trúc **AAA (Arrange - Act - Assert)** với tổng cộng **21 Test Cases**:

### 1. Phân công Unit Test cho 4 thành viên (Mỗi thành viên 4 Unit Tests):
* **Phan Thanh Thịnh (`tests/test_auth.py`):**
  - `test_register_new_user_success`: Đăng ký tài khoản mới hợp lệ.
  - `test_register_duplicate_username_fails`: Đăng ký tài khoản bị trùng username.
  - `test_login_valid_credentials_success`: Đăng nhập với thông tin chính xác.
  - `test_login_wrong_password_fails`: Đăng nhập với mật khẩu sai.
* **Trần Đức Duy (`tests/test_lms.py`):**
  - `test_add_course_success`: Thêm khóa học mới hợp lệ.
  - `test_add_course_duplicate_id_fails`: Thêm khóa học bị trùng mã ID.
  - `test_delete_course_success`: Xóa khóa học thành công.
  - `test_delete_course_not_found_fails`: Xóa khóa học không tồn tại trong hệ thống.
* **Phan Văn Hảo (`tests/test_mentor.py`):**
  - `test_search_mentor_by_skill_found`: Tìm kiếm mentor theo kỹ năng chuyên môn.
  - `test_search_mentor_not_found`: Tìm kiếm mentor với từ khóa không tồn tại.
  - `test_book_appointment_success`: Đặt lịch hẹn tư vấn thành công.
  - `test_session_feedback_invalid_rating_fails`: Đánh giá số sao không hợp lệ (ngoài 1-5 sao).
* **Lê Quân Bảo (`tests/test_documents.py`):**
  - `test_upload_document_success`: Tải lên tài liệu học tập mới.
  - `test_submit_assignment_success`: Sinh viên nộp bài tập.
  - `test_grade_assignment_success`: Giảng viên chấm điểm bài nộp.
  - `test_grade_assignment_not_found_fails`: Chấm điểm bài nộp không tồn tại.

### 2. Hoạt động 3 - Tính phạt mượn sách quá hạn (`tests/test_fine_calculator.py`):
* `test_no_fine`: Trả sách đúng hạn (0 ngày) -> 0đ.
* `test_normal_fine`: Quá hạn 5 ngày -> 25.000đ.
* `test_heavy_fine`: Quá hạn 11 ngày (> 10 ngày) -> 66.000đ (+20%).
* `test_boundary_ten_days`: Quá hạn 10 ngày biên -> 50.000đ.
* `test_negative_days`: Số ngày âm -> 0đ.

### 3. Lệnh chạy kiểm thử tự động (Run Unit Tests):
```bash
# Cách 1: Sử dụng pytest (Khuyên dùng - trực quan, hiển thị tỷ lệ %)
python -m pytest tests/ -v

# Cách 2: Sử dụng thư viện chuẩn unittest có sẵn trong Python
python -m unittest discover -s tests -v
```
