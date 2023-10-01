# Change merge list to dict with using
def merge_list_to_dict(**list_person):
    convert_zip = zip(list_person)
    convert_list = list(convert_zip)
    info_user = f"{list_person}"
    return list_person


print(merge_list_to_dict(name='Arstan', age=19, country="KGS", availy=True))
print(merge_list_to_dict(name="Kamila", age=19, country="KGS", availy=True))


def update_car_info(**car):
    car_dict = dict(car)
    car = {'is_available': True}
    return car


print(update_car_info(brand='Audi', price=12_000))


# Calculate with using names functions

def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multy(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Divide 0 not")
    return a / b


def operation():
    print("access operations:")
    print("1. +")
    print("2.-")
    print("3. *")
    print("4. /")


choose = input("Choose your operation: + - * /  :")

number_1 = input("First num: ")
number_2 = input("Second num: ")

if choose == '1':
    result = add(number_1, number_2)
elif choose == '2':
    result = minus(number_1, number_2)
elif choose == '3':
    result = multy(number_1, number_2)
elif choose == '4':
    result = divide(number_1, number_2)
else:
    print("We are not enter number")

print(f"Result: {number_1} {operation} {number_2} = {result}")
