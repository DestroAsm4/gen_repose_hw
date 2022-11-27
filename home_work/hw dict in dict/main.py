
# Подключение файла функций

from functions import *

# Получение номера студента и формирование строки данных о студенте - students_skills_str

student_number = input('Введите номер студента: ')

students_skills_list = get_student_by_pk(int(student_number))["skills"]

students_skills_str = ''

for students_skill in students_skills_list:
    if students_skill == students_skills_list[len(students_skills_list) - 1]:
        students_skills_str += students_skill
    else:
        students_skills_str += students_skill + ', '

name = get_student_by_pk(int(student_number))['full_name']

# Вывод имени и скилов студента

print(f'Имя студента {name}')
print(f'Студент знает {students_skills_str}')


# Получение названия профессии и формирование строки данных о професии - has, lacks

professions = input('Введите профессию: ')

result = check_fitness(int(student_number), professions)

has = ''
lacks = ''
has_list = result['has']
lacks_list = result['lacks']
for has_skill in has_list:
    if has_skill == has_list[len(has_list) - 1]:
        has += has_skill
    else:
        has += has_skill + ', '

for lacks_skill in lacks_list:
    if lacks_skill == lacks_list[len(lacks_list) - 1]:
        lacks += lacks_skill
    else:
        lacks += lacks_skill + ', '

# Вывод результатов

print(f'Пригодность {round(result["percent"], 2)}%')
print(f'{name} знает: {has}')
print(f'{name} не знает: {lacks}')


