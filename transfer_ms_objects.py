def reduce_person_age(person_red):
    person_red['age'] += -1
    return person_red


person_1 = {
    'name': 'Arstan',
    'age': 19,
    'National': 'Kyrgyzstan'
}

print(reduce_person_age(person_1))


def increase_person_age(person_inc):
    person_inc['age'] -= 1
    return person_inc


person_2 = {
    'name': 'Kamila',
    'age': 18,
    'National': 'Kyrgyzstan'
}

print(increase_person_age(person_2))
print(type(person_2))


def edit_name(avale_ed):
    print(id(avale_ed))
    avale_ed['avaliability'] = None
    return avale_ed


person_3 = {
    'name': 'Arstan',
    'age': 22,
    'avaliability': False

}

print(edit_name(person_3))
print(type(person_3))
print(id(person_3))


def increase_ages(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy

person_4 = {
    'name': 'Aidana',
    'age': 19,
    'id': print(id(person_3))
}

print(increase_ages(person_4))
print(id(person_4))



