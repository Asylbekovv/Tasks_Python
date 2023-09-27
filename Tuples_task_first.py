# Create tuple and print screen
my_tuple = (2313, 3213, 1235, 6456, True, 'STRING')
print(my_tuple)
# Program union tuple
first_union_tuple = (313, ['Sonya', 'Artur', 'Mia'], False, 145.33)
second_union_tuple = (5774,{'company': 'Facebook'}, True, 992.56)
union_all = first_union_tuple, second_union_tuple
print(union_all)
# Create tuple and searching all sum int
tuple_sum = (313, 345, 755, 868, 789, 464)
total_sum = sum(tuple_sum)
print(total_sum)
# Writing tuple with find len
tuple_lens = (131, 134, 645, True, None)
for w in tuple_lens:
    len(tuple_lens)
print(tuple_lens)
# Create tuple containing name different things
tuples_find_things = ('Apple', 'Hamburger', 'Soda', 'Milk', 'Kivi')
elem_find_tuple = "Apple"
if elem_find_tuple in tuples_find_things:
    print(f"Your item was found: {elem_find_tuple}")
else:
    print("Your element not found")




