list_one = ['System', True, 678, None, "Kira"]
list_two = ['Net', False, 313.34, None, "L"]
lists_zip = zip(list_one, list_two)
tuple_list_zip = tuple(lists_zip)
print(tuple_list_zip)
print(type(tuple_list_zip))

students_names_list = ['Artan', 'Aidana', 'Sadat', 'Bektur', 'Ulan']
student_grades_list = [5, 5, 4, 5, 3]
students_zip = zip(students_names_list, student_grades_list)
students_dict = dict(students_zip)
print(students_dict)
print(type(students_dict))

list_len_one = ['Pavel', True, None, 3132, 54.50]
list_len_two = ['Alan', False, {"Name": "Arstanbek"}, 345.77, None, [123]]
list_len_zip = zip(list_len_one, list_len_two)
tuple_len = tuple(list_len_zip)
print(tuple_len)
print(type(tuple_len))

last_names_ls = ['Asylbekov', 'Aliev', 'Minbaev', 'Bazarov', 'Erkinov']
names_ls = ['Arstan', 'Shukur Ali', 'Arsen', 'Bekbol', 'Kubat']
zip_name_ls = zip(last_names_ls, names_ls)
names_list = list(zip_name_ls)
print(names_list)

sum_list_fs = [232, 123, 543, 546, 765, 866]
sum_list_sd = [314, 546, 475, 868, 600, 707]
total_sum = [x + y for x, y in zip(sum_list_fs, sum_list_sd)]
print(total_sum)

country_list_fs = ['USA', 'Kazahstan', 'Italy', 'Spain', 'Canada']
country_city_sd = ['Washington', 'Nursultan', 'Rome', 'Madrid', 'Ottawa']
country_zip = zip(country_list_fs, country_city_sd)
country_dict = dict(country_zip)
print(country_dict)
print(type(country_dict))

letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
numbers_list = [1, 2, 3, 4, 5, 6, 7]
lett_num_zip = zip(letters_list, numbers_list)
lett_num_list = list(lett_num_zip)
print(lett_num_list)
print(type(lett_num_list))

