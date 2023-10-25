try:
    print(100 / 2)
except ZeroDivisionError:
    print("ДАННОЕ ВЫРАЖЕНИЕ НЕ ДЕЛИТСЯ НА 0")

print("Continue...")

my_num = 10
my_str = '10'

try:
    print(my_str + my_num)
except TypeError:
    convert = str(my_num)
    plus = my_str + convert
    print(plus)
print("Two continue...")


