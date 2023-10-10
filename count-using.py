# Counting vowels
vowels_input = input("Введите предложение: ")
vowels = 'a', 'e', 'и', 'о', 'у'
counting = sum(vowels_input.count(i) for i in vowels)
print(f"Гласных букв в предложении: {counting}")

# Consonant counting
consonant_inp = input("Введите второе предложение: ")
consonant_words = 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ'
count = sum(consonant_inp.count(w) for w in consonant_words)
print(f"Согласных букв в предложении: {count}")

# Multiples in count
start = int(input("Введите начало: "))
end = int(input("Введите конец: "))
cn = int(input("Введите определеное число: "))
nums = list(range(start, end + 1))
res = nums.count(cn)
print(f"Количество кратных чисел в диапозоне: {res}")

# Another option
start_diapason = int(input("Enter start diapozone: "))
end_diapason = int(input("Enter end diapozone: "))
multiples_range = int(input("Enter Multiples in a range: "))

numbers = list(range(start_diapason, end_diapason + 1))

result = numbers.count(multiples_range)
print(f"multiples ranges in Diapason: {result}")

# Counting len
count_len_input = str(input("Enter line in string: "))
lens_line = len(count_len_input)
print(f"Lens in string: {lens_line}")
