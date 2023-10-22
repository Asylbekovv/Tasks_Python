# Function for reversed text
def reverse_fn(text):
    value_text = str(' '.join(reversed(text)))
    return value_text


reverse_text_input = input("Enter text: ")
print(reverse_fn(reverse_text_input))

# Lambda functions


plus_use_lambda = lambda a, b: a + b
print(plus_use_lambda(20, 20))


def user_input(input_system):
    pass
    return lambda name: f"{name},{input_system}"


name_input = input("Введите свое имя: ")
authorization = user_input(name_input)
print(f"Пользователь {name_input} вошел в систему!")

# Unpacking dict
telephone_numbers = {
    'Larry': '+996708395187',
    'Emma': '+3554242569659',
    'Omar': '+934958405483',
    'Jeff': '+39-434-5353'
}

users = {
    **telephone_numbers,
    'Larry_is': True,
    'Emma_is': True,
    'Omar_is': True,
    'Jeff_is': False
}
print(users)

print('''---------- ТАБЛИЦА РЕЗУЛЬТАТОВ УМНОЖЕНИЯ ----------''')
print('Таблица умножения на 1')
nums_1 = range(1, 11)
mult_1 = list(map(lambda n: n * 1, nums_1))
print(mult_1)

print('--' * 20)

print("Таблица умножения на 2")
nums_2 = range(1, 11)
mult_2 = list(map(lambda t: t * 2, nums_2))
print(mult_2)

print('--' * 20)

print("Таблица умножения на 3")
nums_3 = range(1, 11)
mult_3 = list(map(lambda tr: tr * 3, nums_3))
print(mult_3)

print('--' * 20)

print("Таблица умножения на 4")
nums_4 = range(1, 11)
mult_4 = list(map(lambda fr: fr * 4, nums_4))
print(mult_4)

print('--' * 20)

print("Таблица умножения на 5")
nums_5 = range(1, 11)
mult_5 = list(map(lambda f: f * 5, nums_5))
print(mult_5)

print('--' * 20)

print("Таблица умножения на 6")
nums_6 = range(1, 11)
mult_6 = list(map(lambda si: si * 6, nums_6))
print(mult_6)

print('--' * 20)

print("Таблица умножения на 7")
nums_7 = range(1, 11)
mult_7 = list(map(lambda se: se * 7, nums_7))
print(mult_7)

print('--' * 20)

print("Таблица умножения на 8")
nums_8 = range(1, 11)
mult_8 = list(map(lambda ei: ei * 8, nums_8))
print(mult_8)

print('--' * 20)

print("Таблица умножения на 9")
nums_9 = range(1, 11)
mult_9 = list(map(lambda ni: ni * 9, nums_9))
print(mult_9)


# Использование Lambda для приветствия пользователя!
def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greet = greeting("Доброе утро")
print(morning_greet("Арстан"))


# Использование Lambda для входа в систему!
def welcome_site(sign):
    return lambda user_s: f"{user_s}, {sign}!"


user_commander = welcome_site("Вошел в систему")
print(user_commander("Арстан"))

