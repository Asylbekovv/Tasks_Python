people_1 = {
    'name': 'Dave',
    'age': '32',
    'address': 'st.Lincoln'
}

people_2 = {
    'name': 'Jessica',
    'age': '22',
    'address': 'st.Abram'
}
print("--Peoples--Names--")
for i in range(0, 1):
    name_people_1 = people_1['name'.lower()]
    print(name_people_1)

for j in range(0, 1):
    name_people_2 = people_2['name'.lower()]
    print(name_people_2)

print("--Ages--People")
for i in range(1):
    age_people_1 = people_1['age'.lower()]
    print(age_people_1)

for j in range(1):
    age_people_2 = people_2['age'.lower()]
    print(age_people_2)

print("--Address--People")
for m in range(1):
    address_people_1 = people_1['address'.lower()]
    print(address_people_1)

for j in range(1):
    address_people_2 = people_2['address'.lower()]
    print(address_people_2)
print("Full information peoples")
print(people_1)
print(people_2)








