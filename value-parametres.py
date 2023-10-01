from datetime import date


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 123,
    'author': 'Arstan'
}

post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)


def get_month_day():
    return date.today()


def create_user_post(user, month=get_month_day()):
    user_copy = user.copy()
    user_copy =['created_with_month']
    return user_copy

initial_user = {
    'id': 888,
    'author': 'Kairat'
}
print(create_user_post(initial_user))
