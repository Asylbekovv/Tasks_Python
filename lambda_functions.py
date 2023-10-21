# Function for reversed text
def reverse_fn(text):
    value_text = str(' '.join(reversed(text)))
    return value_text


reverse_text_input = input("Enter text: ")
print(reverse_fn(reverse_text_input))

# Lambda functions


plus_use_lambda = lambda a, b: a + b
print(plus_use_lambda(20, 20))


def user_input(input_system):
    return lambda name: f"{name},{input_system}"
name_input = input("Введите свое имя: ")
authorization = user_input(name_input)
print(f"Пользователь {name_input} вошел в систему!")

