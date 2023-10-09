a = 10


# Global Scope


def my_fn():
    # Local Scope
    def inner_fn():
        print(a)
        inner_fn()


my_fn()

c = 15


# Global Scope
def my_new_fn():
    c = True
    b = 90
    print(c)
    print(b)


my_new_fn()
print(c)

print("Welcome to my calculate!")
print("---" * 20)
print("Enter: 1 use plus")
print("Enter: 2 use minus")
print("Enter: 3 use multi")
print("Enter 4 use divide")
choose_operation = int(input("Choose operation | + | - | * | / |: "))
first_num = float(input("Enter your first number: "))
second_num = float(input("Enter your second number: "))


def plus(sum_1, sum_2):
    result = sum_1 + sum_2
    return result


def minus(sum_1, sum_2):
    return sum_1 - sum_2


def multi(sum_1, sum_2):
    result = sum_1 * sum_2
    return result


def divide(sum_1, sum_2):
    result = sum_1 / sum_2
    return result


if choose_operation == 1:
    print(f"Result: {plus(first_num, second_num)} ")
elif choose_operation == 2:
    print(f"Result: {minus(first_num, second_num)} ")
elif choose_operation == 3:
    print(f"Result: {multi(first_num, second_num)} ")
elif choose_operation == 4:
    print(f"Result: {divide(first_num, second_num)} ")
else:
    print("You dont enter operation")

close = input("want to exit: ")
if close == 'yes':
    print("See you later :)")
