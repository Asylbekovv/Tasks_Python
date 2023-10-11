# List for adding numbers
simple_list = []
while True:
    workers_input = input("Enter integers add in list: ")
    if workers_input.lower() == 'exit':
        break
    else:
        simple_list.append(workers_input)
print(simple_list)
# List for adding games and after converting tuple
games_list = []
while True:
    game_input = input("Enter game to add tuples: ")
    if game_input.lower() == 'exit':
        break
    games_list.append(game_input)
    convert = tuple(games_list)
    print(convert)
