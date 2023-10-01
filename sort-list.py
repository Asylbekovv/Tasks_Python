# Sort list with sort function
def sort_list(f_list):
    f_list.sort()
    return f_list


first_list = [2, 4, 6, 8, 3, 5, 7]
print(sort_list(first_list))


# Sort list with reverse sort function
def sort_list_reversed(r_list):
    r_list.sort(reverse=True)
    return r_list


reversed_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sort_list_reversed(reversed_list))
