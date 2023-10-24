import random

print('''----------------Рандомайзер случайных чисел----------------''')
random_num = random.randint(1, 100)
print(f"Ваше число: {random_num}")

print('''----------Рандомайцер с выбором начала и конца!----------''')


def random_num(num_1, num_2):
    result = random.randint(int(num_1), int(num_2))
    print(f"Результат вашего запроса: {result}")


ones_random_input = input(f"Введите начало: ")
twos_random_input = input(f"Ввелите конец: ")
print(random_num(ones_random_input, twos_random_input))

print('''----------Выбор рандобного элемента списка----------''')
random_list = ['Python', 'Develop', True, 766, None]
random_elemet = random.choice(random_list)
print(f"Случайный элемент в списке: {random_elemet}")

print("----------Орел и Решка---GAME----------")

games_eagle_tails = ['Орел', 'Решка']
games_chose = random.choice(games_eagle_tails)
print(f"Результат игры:  {games_chose}")

print("Камень, Ножницы, Бумага---ИГРА")
choose_r_p_s = random.randint(1, 3)

if choose_r_p_s == 1:
    res1 = choose_r_p_s == 'Камень'
    print(res1)
elif choose_r_p_s == 2:
    res2 = choose_r_p_s == 'Ножницы'
    print(res2)
elif choose_r_p_s == 3:
    res3 = choose_r_p_s == 'Бумага'
    print(res3)

print(f"Итог игры: {choose_r_p_s}")

# Другой вариянт
print("-----Rock|Paper|Scissors-----")
data_game = ['Камень', 'Ножницы', 'Бумага']
game_rock_paper_scissors = random.choice(data_game)
print(f"Результат игры: {game_rock_paper_scissors}")

