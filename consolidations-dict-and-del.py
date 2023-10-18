# How long does a person live country in use dict and union
country_dict = {
    'USA': 'Washington',
    'Spain': 'Madrid',
    'Italy': 'Rome',
    'Kyrgyzstan': 'Bishkek',
    'France': 'Paris',
    'England': 'London'
}

people_in_country = {
    'Washington': "689545 peoples",
    'Madrid': "328000 peoples",
    'Rome': "2758000 peoples",
    'Bishkek': "7000000 peoples",
    'Paris': "2148327 peoples",
    'London': "648110 peoples",
}

info = country_dict | people_in_country

for key in info:
    print(f"{key} -- {info[key]}  ")

new_dict = {
    'local': 'net',
    'global': 'com'
}
conv_dict = list(new_dict)
conv_dict.__delitem__(0)
conv_dict.append('Host')
print(conv_dict)
print("--" * 20)

string_list = ['ABC', '123,', 'Keep going', 'Local host']
for j in string_list:
    print(j)

user_n_p_list = []
for _ in range(5):
    input_name = input("Введите свое имя: ")
    greeting = f"Привет, {input_name} добро в админку для добавления данных!"
    print(greeting)
    input_password = input("Введите свой пароль: ")
    user_n_p_list.append(f"Ваши данные:  имя:  {input_name}, пароль:  {input_password} ")
    print('\n'.join(user_n_p_list))













