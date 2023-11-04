# Найти уникальные элементы в списке
unique_list = [100, 200, 300, 400, 400, 200, 300, 100]
unique_set = set(unique_list)
print(unique_set)


# Найти уникальные слова в тексте


def unique_words(text):  # Function for search unique words in text
    words = text.lower().split()
    unique_word = set(words)
    return len(unique_word)


unique_input = input("Enter your text: ")
unique_output = unique_words(unique_input)

print(f"Count unique words: {unique_output}")

# Найти пересечение двух списков
j_list = ['L', 'Manhwa', 'Manga', 'Paper', 'Pen']
i_list = ['Manhwa', 'Manga', 'L', 'Pencil', 'Marker']
j_i_intersection = set(j_list).intersection(set(i_list))
print(f"Intersection list: {j_i_intersection}")
print(j_i_intersection)



