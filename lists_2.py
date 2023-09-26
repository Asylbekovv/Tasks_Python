# Нахождение среднего значения списка
print("Наш список")
this_list = [1, 22, 56, 99, 54]
print(this_list)
result = sum(this_list)
convert_int = int(result)
list_len = len(this_list)
average_total = result / list_len
print('Среднее арифметическое списка: ')
print(average_total)

#Нахождение наибольшего и наименшего элемента в
print("Нахождение наибольшего и наименшего элемента в списке")
greatest_list = [32, 13, 45, 654, 565, 534]
print("Наибольший элемент")
print(max(greatest_list))
print("Наименьший элемент")
print(min(greatest_list))
print("Длинна списка")
print(len(greatest_list))

# Поиск элемента в списке
print("Поиск элемента в списке")
list_element = [1334, 4423, 5345, 6756, 5676]
search_elem = ...
if search_elem in list_element:
    print(f"Ваш элемент: {search_elem}")
else:
    print(f"Вы не ввели элемент!")

#Второй вариант поиска в списке
print("Hello welcome to program for searching element List!")
name = input("Please Enter your name: ")
print(f'Good afternoon dear {name}')
list_s = []
list_s_range = list(range(0, 5))
list_input = input("Please enter your elements for list: ")
for i in range(list_input):
    elem = input(int(f"Введите количество {i + 1}"))
    list_s.append(elem)
print(list_s)






