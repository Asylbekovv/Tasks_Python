import datetime

# Students dictionary
students = {
    'name': 'Arstan',
    'age': 19,
    'identification': 100,
    'born_data': datetime.date(2004, 9, 3)
}
print(students)

print("--" * 40)

students_dict = {}

students_dict['Arstan'] = {'age': 19, 'identification': 213, 'born': '2004-09-03'}
arstan_info = students_dict['Arstan']
print("Information about student Arstan")
print(f"Age student: {arstan_info['age']}")
print(f"Info ID student: {arstan_info['identification']}")
print(f"Date of Brith: {arstan_info['born']}")

print("--" * 40)

students_dict['Alex'] = {'age': 20, 'identification': 214, 'born': '2003-07-11'}
alex_info = students_dict['Alex']
print("Information about student Alex")
print(f"Age student: {alex_info['age']}")
print(f" Info ID student: {alex_info['identification']}")
print(f"Date of Brith: {alex_info['born']}")

print("--" * 40)

students_dict['Mia'] = {'age': 19, 'identification': 215, 'born': '2004-05-20'}
mia_info = students_dict['Mia']
print("Information about student Mia")
print(f"Age student: {mia_info['age']}")
print(f"Info ID student: {mia_info['identification']}")
print(f"Date of Brith: {mia_info['born']} ")

print("--" * 40)
print("The end")

