import statistics

# Среднее арифметическое
average_list = [12, 33, 44, 65, 34, 88]


def average(ave_sum):
    ave_sum = sum(average_list) / len(average_list)
    return ave_sum


print(average(average_list))

average_num1 = int(input("Введите первое число: "))
average_num2 = int(input("Введите второе число: "))


# Нахожнение среднее арифметического числа с помощью statistics

def average_inputs(a, b):
    res_sum = a, b
    average_value = statistics.mean(res_sum)
    return average_value


print(f"Cреднее арифметическое двух чисел:", average_inputs(average_num1, average_num2))

white_list = []


def average_function(q, n):
    m = (q + n) / 2
    return m


q_input = int(input("First num: "))
n_input = int(input("Second num: "))
print("Average two nums:", average_function(q_input, n_input))

name = input("Enter name: ")
greet = f"Welcome {name}!"
print(greet)
