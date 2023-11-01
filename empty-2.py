# Task with use concatenate str and output in console
first_str = "Hello "
second_str = "Arstan"
concatenable_text = first_str + second_str
print(concatenable_text)

user_name = input("Enter your name: ")
greeting_user = f"Hello {user_name} welcome to site"
print(greeting_user)
PASSWORD = 23423323
user_password = input("Enter your password: ")
output_password = f"Your account password: {user_password} is confirm"
print(output_password)

# Task with use sets methods
a_set = {220, 343, 435, 456, 76, 757, 6456}
b_set = {223, 343, 220, 354, 67, 6456, 566}
intersection_sets = a_set.intersection(b_set)
another_intersection = a_set | b_set
print(another_intersection)
print(intersection_sets)
is_sub_set = b_set.issubset(a_set)
print(is_sub_set)


# Task with use tuples
students = (('Alina', 67, 18),
            ('Aidana', 100, 18),
            ('Aidar', 55, 19),
            ('Sultan', 88, 18))

students_names = [name[0] for name in students]
print("Students names", ' '.join(students_names))


def students_names_fn(std):
    empty_str = ' '
    std = [std[0] for std in students]
    print("Student another variant: ", empty_str.join(std))

print(students_names_fn(students))


def plus(num_1, num_2):
    count = +1
    res = count + num_1 + num_2
    print(res)

num_1_inp = int(input("Enter first num: "))
num_2_inp = int(input("Enter second num: "))
print("Result: ", plus(num_1_inp, num_2_inp))
print("Hello world")


