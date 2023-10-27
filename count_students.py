all_students = [
    ('Nihojin', 19, 67.22),
    ('Anya', 10, 30.12),
    ('Denki', 18, 80.66),
    ('Haruko', 20, 76.68)
]
print("----Студенты у которых больще 90!----\n")
for student_more in all_students:
    if student_more[2] > 90:
        print(f"У {student_more[0]} больше 90 баллов")
print("----Студенты у  которых меньше 90 баллов----\n")
for student_little in all_students:
    if student_little[2] < 90:
        print(f" У {student_little[0]} меньше 90 баллов на перездачу!")

new_student_1 = ('Nera', 23, 91.22)
all_students.append(new_student_1)
new_student_2 = ('Ayaka', 21, 77.88)
all_students.append(new_student_2)

print("----Отсортированные по возрасту----\n")
for sorted_age in all_students:
    all_students.sort(key=lambda n: n[2])
    print(f"Сортировка студентов во возрасту: {sorted_age[2]}")




