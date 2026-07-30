students = [
    {"name": "An", "gpa": 7.2},
    {"name": "Bình", "gpa": 9.5},
    {"name": "Cường", "gpa": 6.8},
    {"name": "Dũng", "gpa": 8.4}
]


def bubble_sort_gpa_descending(student_list):
    n = len(student_list)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if student_list[j]["gpa"] < student_list[j + 1]["gpa"]:
                student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]
                swapped = True
        if not swapped:
            break
    return student_list


def print_ranking(student_list):
    print("BẢNG XẾP HẠNG SINH VIÊN (BUBBLE SORT - GPA GIẢM DẦN)")
    for rank, student in enumerate(student_list, start=1):
        print(f"Top {rank}: {student['name']} - {student['gpa']} điểm")


if __name__ == "__Bai2__":
    ranked_students = bubble_sort_gpa_descending(students)
    print_ranking(ranked_students)
