list_a = [1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
for j in list_a:
    if j < 5:
        print(f"Эти элементы меньше нуля: {j} ")

    elif j > 5:
        print(f"Эти элементы больше пяти: {j}")

convert_list_to_tuple = tuple(list_a)
all_res = {convert_list_to_tuple for j in range(1, 6)}
print(f"Все элементы в списке: {all_res}")
# Первый вариант решения через конвертацию
a_list = [1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
general_in_set1 = set(a_list)
general_in_set2 = set(b_list)
general = general_in_set1.intersection(b_list)
print(f"Общее элементы в списке: {general}")

# Второй вариянт решения

a = [2, 1, 3, 5, 6, 8, 9, 22, 66, 77]
b = [1, 2, 3, 4, 5, 6, 7, 77, 22, 9]
result_list = list(set(a) & set(b))
print(f"Результат общих элементов: {result_list}")
result_union = list(set(b) | set(a))
print(f"Обьединение наборов: {result_union}")
