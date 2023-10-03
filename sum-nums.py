m = {122, 435, 546, 756, 345}
n = {313, 435, 424, 345, 234}
inter_m_n = m.intersection(n)
issubset_m_n = n.issubset(m)
union_m_n = m.union(n)
superset_m_n = n.union(m)
print(inter_m_n)
print(issubset_m_n)
print(union_m_n)
print(superset_m_n)


def count_sym(quantity, quantity_tuple):
    quantity_tuple = tuple()
    quantity = len(quantity_tuple)
    res = quantity, quantity_tuple
    return res


tuples = ("Python", "Async", "Repository")
print(tuples)


def search_count(sym):
    count = 0
    for elem in sym:
        count += 1
        return count


component_tuples = (123, "Python", "Async", "Repository", False)
print(search_count(component_tuples))
