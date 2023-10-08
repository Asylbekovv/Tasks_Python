# Reversed str with use input
str_intput = input("Enter string: ")
reverse_str = "".join(reversed(str_intput))
print(reverse_str)

# Searching vowels
print('--' * 20)
print("Программа для нахождения гласных букв в предложении!")
vowels_c = input("Введите строку: ")
vowels_count = 0
vowels_set = ('a', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я')
for i in vowels_c:
    if i in vowels_set:
        vowels_count += 1
print(f"В данной строке {vowels_c} гласных букв {vowels_count}")

# Searching consonant
print('--' * 20)
print("Программа для нахождения согласных букв в предложении!")
consonant_input = input("Введите строку: ")
consonant_count = 0
consonaut_set = (
'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
for i in consonant_input:
    if i in consonaut_set:
        consonant_count += 1
print(f"В данной строке {consonant_input} согласных букв {consonant_count}")

# Delete spaces
print("--" * 20)
print("Программа для удаления пробелов в предложении!")
spaces_input = input("Введите предложение: ")
spaces_without = spaces_input.replace(" ", '')
print(f"Удаленный вариянт предложения:  {spaces_without}")


# Double spaces
print('--' * 20)
print("Программа двойного пробела!")
double_spaces = input("Введите предложение: ")
spaces_double = double_spaces.replace('', '  ')
print(f"Вариянт предложения с двойными пробелами {spaces_double}")

print("Конец программы!")
