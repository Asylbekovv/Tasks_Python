# Intersections set
a_box = (1312, 123, 245, 345, 466, 6765, 567, 567)
b_box = (123, 345, 5546, 456, 453, 234, 6575, 453)
intersect_box_a = set(a_box)
intersect_box_b = set(b_box)
conv_a_and_b = intersect_box_a.intersection(intersect_box_b)
print(f"Одинаковые числа в наборе: {conv_a_and_b}")
# Union set
union_a_box = set(a_box)
union_b_box = set(b_box)
conv_union_a_and_b = union_a_box.union(union_b_box)
print(f"Обьединение наборов: {conv_union_a_and_b}")
issub_a_box = set(a_box)
issub_b_box = set(b_box)
# issubset set first box
issubset_a_and_b = issub_a_box.issubset(b_box)
print(f"Является ли A подмножеством B: {issubset_a_and_b}")
# issubset set second box
issubset_b_and_a = issub_b_box.issubset(issub_a_box)
print(f"Является ли B подмножеством A: {issubset_b_and_a}")

