pc_programs = ['Microsoft Word', 'Paint', 'Power Point', 'PowerShell']
pc_prog_rams = [440, 330, 100, 500]
using_in_pc = (True, True, True, False)
all_programs_zip = zip(pc_programs, pc_prog_rams, using_in_pc)
all_list = list(all_programs_zip)
print(all_list)
difference_first = {12, 33, 54, 67, 98, 75}
difference_second = {33, 12, 44, 65, 67, 200}
difference_first.add(200)
sets_intersection = difference_first.intersection(difference_second)
sets_uni = difference_first.union(difference_second)
dif_list = list(difference_first)
dif_list_2 = list(difference_second)
print(dif_list, dif_list_2)
print(sets_intersection,sets_uni)
print(type(difference_first))



