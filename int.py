from copy import deepcopy


# Not changeable objects
number_one = 10
number_two = number_one
print(id(number_one))
print(id(number_two))

# Changeable objects
my_list = [1, 2, 3]
print(id(my_list))
print(type(my_list))
other_list = [1, 2, 3, 4]
print(id(other_list))
print(type(my_list))
new_list = [1, 2, 3]
print(id(new_list))
print(type(my_list))

# Dicts
info = {'user': 'Arstan', 'is_instructor': True}
info_copy = info
info['reviews_qty'] = 10
info_copy['reviews_qty'] = 400
print(info)
print(info_copy)
# Working with Dicts and conversion in List
info_second = {'user': 'Jack', 'is_instructor': False}
info_second_new = info_second
info_second_new['Work'] = True
conversion_list = list(info_second_new)
print(conversion_list)
print(type(conversion_list))
print(id(conversion_list) > id(info_second_new))

# Avoid copy changes
my_information = {
    'name': 'Arstan',
    'age': '19',
    'reviews': []
}

new_information = my_information.copy()
new_information['reviews'].append('Program')
print(my_information)
print(new_information)
# Use Deepcopy import copies method
second_information = {
    'name': 'Mery',
    'age': '19',
    'availability': []
}
second_deepcopy = deepcopy(second_information)
second_deepcopy['availability'].append(True)
print(second_information)
print(second_deepcopy)
print(id(second_information))








