my_list = [1, 2, 2, 1, 4, 5, 6, 7, 7, 8]
search_unique = set(my_list)
print(f"Количество уникальных элементов: {search_unique}")

first_list = [1, 2, 3, 4, 5]
second_list = [3, 4, 5, 6, 7]
all_elem = list(set(first_list) & set(second_list))
print(all_elem)


