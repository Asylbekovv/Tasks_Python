my_list = [1, 2, 2, 1, 4, 5, 6, 7, 7, 8]
search_unique = set(my_list)
print(f"Количество уникальных элементов: {search_unique}")

first_list = [1, 2, 3, 4, 5]
second_list = [3, 4, 5, 6, 7]
all_elem = list(set(first_list) & set(second_list))
print(all_elem)

def sum_nums(*args):
    print(args)
    print(type(args))
    return sum(args)


print(sum_nums(122, 323, 667))


def post_qty_info(name, posts):
    info = f"Hello {name} you have {posts} posts"
    return info

info_user = post_qty_info('Arstan', 220)
print(info_user)
print(type(info_user))

def get_email_pass(number, email, password):
    get_info = f"User: {number} Email: {email} \nPassword: {password}\n"
    return get_info

user_01 = get_email_pass(number=1, email="asylbekov20love@gmail.com", password=2102023)
user_02 = get_email_pass(number=2, email="kamila009@gmail.com", password=2331324)
user_03 = get_email_pass(number=3, email="aidanaofficial223@gmail.com", password=32423453)

print(user_01, user_02,user_03)

