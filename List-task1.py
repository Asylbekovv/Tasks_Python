elem_list = [123, True, 'Python', 22.66, {'a': None}]
del elem_list[3]
print(len(elem_list))
elem_list.reverse()
second_list = ['World', False]
elem_list.extend(second_list)
print(elem_list)
