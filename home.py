mentors = [
    {"name": "Nguyen Van A", "skill": "Python"},
    {"name": "Tran Van B", "skill": "Java"},
    {"name": "Le Van C", "skill": "Python"}
]


def search_mentor(keyword):
    result = []

    for mentor in mentors:
        if keyword.lower() in mentor["skill"].lower():
            result.append(mentor)

    return result


if __name__ == "__main__":
    keyword = input("Nhap ky nang muon tim: ")

    result = search_mentor(keyword)

    if result:
        print("Danh sach Mentor:")
        for mentor in result:
            print(mentor["name"], "-", mentor["skill"])
    else:
        print("Khong tim thay Mentor!")