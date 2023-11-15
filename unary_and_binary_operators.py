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

# unary operators
unary_op = 200
print(-unary_op)
# binary operators
binary = True
print(+binary)
print(-binary)
comparison = unary_op and binary
comparison_with_use_or = binary or unary_op
print(comparison_with_use_or)
print(comparison)

bmw = {
    'brand': 'BMW',
    'price': 200_000,
    'motor': 'V8',
    'achive': {
        'achivable': True
    }
}

print('brand' in bmw)
print('achive' not in bmw)
print('motor' and 'achive' in bmw)
print('achive' in 'achivable' in bmw)


print("Первый набор")
cp1_set = {123, 131, 245, 535, None, 'set'}
print("Второй набор")
cp2_set = {123, 131, 245, 535, None, 'set'}
print("Сравнение двух наборов с использованием is")
print(cp1_set is cp2_set)  # False
print("Сравнение двух наборов с помощью оператора сравнения")
print(cp1_set == cp2_set)  # True
print("Есть ли в наборе какой либо элемент")
print(245 in cp2_set)  # True
print(300 in cp1_set)  # False

cp3_set = set()
cp4_set = cp3_set
cp3_4set = cp3_set == cp4_set
print(cp3_set is cp3_4set)
print(cp3_4set)
