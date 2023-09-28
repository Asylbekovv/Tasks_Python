# Union a - b sets
a = {1, 2, 3}
b = {4, 5, 6}
a_b_union = a.union(b)
print(a_b_union)
print(type(a_b_union))
# intersection sets
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
x_y_inter = x.intersection(y)
print(x_y_inter)
# Difference sets
p = {1, 2, 3, 4, 5}
q = {3, 4}
diff_p_q = p.difference(q)
print(diff_p_q)
# Issubset set
m = {1, 2, 3}
n = {1, 2, 3, 4, 5}
is_sub_m_n = m.issubset(n)
print(is_sub_m_n)
# Lens set
z = {5, 10, 15, 20, 25}
lens_z = len(z)
print(lens_z)

numbers = [1, 2, 2, 3, 4, 4, 5]
uni_nums = set(numbers)
print(uni_nums)
