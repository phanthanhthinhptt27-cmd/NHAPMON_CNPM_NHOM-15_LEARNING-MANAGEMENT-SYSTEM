def book_appointment():
    mentor = input("Nhap ten Mentor: ")
    date = input("Nhap ngay hen: ")
    time = input("Nhap gio hen: ")

    print("\nDat lich thanh cong!")
    print("Mentor:", mentor)
    print("Ngay hen:", date)
    print("Gio hen:", time)


if __name__ == "__main__":
    book_appointment()