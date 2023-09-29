def merge_list_to_dict(first_list, second_list):
    convert_zip = zip(first_list, second_list)
    convert_list = list(convert_zip)
    conv_dict = dict(convert_list)
    return first_list, second_list


person_1 = ["Arstan", 19, 'Kyrgyzstan', True]
person_2 = ["Aidana", 19, "Kyrgyzstan", True]

print(merge_list_to_dict(person_1, person_2))
print(type(merge_list_to_dict))


def intersect(set_1, set_2):
    intersect_set = set_1.union(set_2)
    convert_list = list(intersect_set)
    return set_1, set_2

new_set_first = {111, True, 423}
new_set_second = {4324, None}
print(intersect(new_set_first, new_set_second))


def know_tuple_count(tuple_count):
    print(tuple_count.count(f"{first_tuple}"))
    return tuple_count

first_tuple = ('Asylbekov', 123, 24.23)
print(know_tuple_count(first_tuple))

print(merge_list_to_dict([123, 'a', 'b', 'c'], [True, [], None]))
print(intersect({123, 434, 555, 656}, {331, 323, 555, 123}))


def list_to_dict(user_1, user_2):
    conv_zip = zip(user_1, user_2)
    conv_dict = conv_zip
    return user_1, user_2

user_1_l = [4354, True, False]
user_2_l = [242, 'abc', None, True]
result_dict = (user_1_l, user_2_l)
print(list_to_dict(user_1_l, user_2_l))
print(type(result_dict))
