# Operator (not) return revision output
print(not 10)  # False
print(not False)  # True
print(not 0)  # True
print(not True)  # False

print(not [])  # True
print(not {})  # True
white_list = [1, 2, 3]  # False
print(not not white_list)  # True
print(not None)  # True

other_list = ['a', 'b', 'c']
print(bool(other_list))
print(not other_list)
print(not not other_list)

my_list = [1, 2, 3]
print(bool(my_list))
print(f"Результат выражения: ", my_list or other_list)
print(f"Результат второго выражения: ", other_list and my_list)
another_list = (None, False)
print("Результат третьего выражения: ", my_list and another_list)
print("Результат четвертого выражения: ", another_list or my_list)
print(bool(another_list))

print(len(my_list) > 0 and another_list)
print(bool(len(another_list) > 0 and my_list))

first_dict = {
    'usa': 'Washington',
    'spain': 'Madrid',
    'italy': 'Rime'
}

print(f"Результат первого словоря: ", first_dict)

second_dict = {
    'italy': 'Rime',
    'usa': 'Washington',
    'spain': 'Madrid'
}

print("Результат второго словоря: ", second_dict)

first_dict == second_dict and print("Dictionary are equal")
first_dict != second_dict and print("The first list is not equal to the second")
second_dict != first_dict or print("First and Second dict are equal")
second_dict != first_dict or print("First and Second dict are equal")

