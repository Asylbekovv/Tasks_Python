# Программа заметки!
empty_notes = {}


# Эта функция используется для добавления заметки
def add_task():
    node_id = len(empty_notes) + 1
    node_text = input("Введите заметку: ")
    empty_notes[node_id] = node_text
    print(f"{node_id} Ваша заметка добавлена!")


# Эта функция используется для просмотра заметок

def view_notes():
    for node_id, node_text in empty_notes.items():
        print(f"Заметка под номером №{node_id}: {node_text}")


# Тут используется бесконечный цикл с выбором операций
while True:
    print("Выберите действие:")
    print(" 1- добавить заметку ")
    print(" 2- посмотреть заметки ")
    print(" 3- выйти")

    choose_op = input("Введите операцию: ")
    if choose_op == '1':
        print(add_task())
    elif choose_op == '2':
        print(view_notes())
    else:
        print("Спасибо что воспользовались нашей программой)")
        break
