# Create empty dict for storage information
notes_db = {}


# This function uses for added task in note


def add_note():
    note_number = len(notes_db) + 1
    note_text = input("Enter your task: ")
    notes_db[note_number] = note_text
    print("Your task is added note")


# This function uses for view information in note

def views_note():
    for note_number, node_text in notes_db.items():
        print(f"Your task of number {note_number}: {node_text}")


# This function uses for delete task on note


def delete_task():
    if not notes_db:
        print("notes empty")
        return


while True:

    print('''---Choose your operation---
    1. Choose 1. for add task in note
    2. Choose 2. for view information
    3. Choose 3. for delete task
    4. Choose 4. Exit''')

    choose = input("Enter operation: ")

    if choose == '1':
        print(add_note())
    elif choose == '2':
        print(views_note())

    elif choose == '3':
        if choose in notes_db:
            del_task = notes_db.pop(choose)
            print(delete_task())
    else:
        print("See you later)")
