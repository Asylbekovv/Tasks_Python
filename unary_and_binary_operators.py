# Comparison Lists with method __eq__
white_list = [1, 3]
black_list = [1, 4]
print(white_list == black_list)
print(white_list.__eq__(black_list))

# Comparison with using input

black_input = list(input("Введите первый список для сравнения: "))
white_input = list(input("Введите второй список для сравнения: "))
res_list = (black_input.__eq__(white_input))
print(res_list)
# Convert list to tuple and dict print result console

black_new = list(input("Введите первый список для конвертации: "))
white_new = list(input("Введите второй список для конвертации: "))
black_tuple = tuple(black_new)
white_tuple = tuple(white_new)
res_tuple_zip = zip(black_tuple, white_tuple)
conv_zip = dict(res_tuple_zip)
print(conv_zip)

print(dir(list))
# Sorted function
list_sort_input = list(input("Введите список для сортировки: "))
list_sorted = sorted(list_sort_input)
print("Результат сортировки списка: ", list_sorted)
