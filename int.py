# Not changeable objects
number_one = 10
number_two = number_one
print(id(number_one))
print(id(number_two))

# Changeable objects
my_list = [1, 2, 3]
print(id(my_list))
print(type(my_list))
print()
other_list = [1, 2, 3]
other_list.append(4)
print(id(other_list))
print(type(my_list))
new_list = [1, 2, 3]
print(id(new_list))
print(type(my_list))





