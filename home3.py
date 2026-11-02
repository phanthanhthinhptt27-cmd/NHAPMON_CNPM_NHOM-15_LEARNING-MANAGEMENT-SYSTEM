def session_feedback():
    mentor = input("Nhap ten Mentor: ")

    rating = int(input("Danh gia Mentor (1-5 sao): "))

    feedback = input("Nhap noi dung phan hoi: ")

    if rating < 1 or rating > 5:
        print("Danh gia khong hop le!")
    else:
        print("\nDanh gia thanh cong!")
        print("Mentor:", mentor)
        print("So sao:", rating)
        print("Phan hoi:", feedback)


if __name__ == "__main__":
    session_feedback()