first_list = [123, 'Other world', True]
second_list = [None, 77.22, False]
# first variant output
merged_list = first_list + second_list
# second variant output
print(first_list.__add__(second_list))



