import random

random_generate = random.randint(1, 100)
print("---Напишите --> yes чтобы запустить программу!")
print("---Напшите --> no чтобы закрыть программу!")
start_input = input("Запуск: ")
if start_input == 'yes':
    print(random_generate)
elif start_input == 'no':
    exit()
else:
    print("Ошибка :)")


def reversed_str(text):
    reverse_text = str(' '.join(reversed(text)))
    return print(f"Перевернутый текст: {reverse_text}")


text_reverse_inp = str(input("Введите текст: "))
print(reversed_str(text_reverse_inp))


plus_fn = lambda a, b: a + b
calc_elem_1 = int(input("Введите первое число: "))
calc_elem_2 = int(input("Введите второе число: "))
print(plus_fn(calc_elem_1, calc_elem_2))

minus_fn = lambda n, m: n - m
calc_elem_3 = int(input("Enter first number: "))
calc_elem_4 = int(input("Enter second number: "))
print("Result: ", minus_fn(calc_elem_3, calc_elem_4))

full_list = ['Response', 'Loki', 'Deep', 'Adam', 'lock', 'Cyber', 'Open AI']
for j, count in full_list:
    print(count + 1, j)






