# Operator (is)
value_a = 100
value_b = value_a
c = 300
d = 300
f = d + c
print(value_a is value_b)
print(c is value_b)  # Operator use for comparison 2 values which each other
print(d is f)
print(c is d)

# Comparison first and second obj
first_obj = 1_000_000
second_obj = 1000000
print("Результат сравнения двух обьектов: ", first_obj is second_obj)

# This program comparison 2 obj and output result

one_input = input("Введите первый обьект: ")
two_input = input("Введите второй обьект: ")
comparison_obj = one_input is two_input

print("Результат сравнения равен: ", comparison_obj)

group_peoples_1 = ['Aluca, Kevin, Mika, Nasumi']
group_peoples_2 = ['Sukuna', 'Gojo', 'Yuta']
copy_group = group_peoples_2.copy()
print(copy_group is group_peoples_2)
print(copy_group)
print(group_peoples_2)

obj_1 = (input("Введите первый обьект: "))
obj_2 = (input("Введите второй обьект: "))


def comparison(a, b):
    a = b
    b = a
    c = a is b
    return c


print("Результат сравнения: ", comparison(obj_1, obj_2))
