
# Обьявление импротов

import json
import os

# Константы fills_path: набор путей используемых файлов

fills_path = {'students': 'students.json', 'professions': 'professions.json'}


def load_students(path):
    """

    :param path: получает путь к json файлу со списком студентов
    :return: выводит данные о студентах в виде списка словарей
    """
    with open(os.path.join(path), 'rt', encoding='utf-8') as fille_students:
        students_list = json.load(fille_students)
    return students_list


def load_professions(path):
    """

    :param path: получает путь к json файлу со списком профессий
    :return: выводит данные о профессиях в виде списка словарей
    """
    with open(os.path.join(path), 'rt', encoding='utf-8') as fille_professions:
        professions_list = json.load(fille_professions)
    return professions_list


def get_student_by_pk(pk):
    """

    :param pk: получает число - номер студента
    :return: выводит данные о студенте в виде слоавря или строку об исключении
    """
    result = None
    students = load_students(fills_path['students'])
    for student in students:
        if student['pk'] == pk:
            result = student
    if result is None:
        result = 'У нас нет такого студента'
    return result


def get_profession_by_title(title):
    """

    :param title: получает название профессии в виде строки
    :return: возвращает словарь с данными о требованиями для профессии или строка об отсутствии профессии
    """
    result = None
    professions = load_professions(fills_path['professions'])
    for profession in professions:
        if profession['title'] == title:
            result = profession
    if result is None:
        result = 'У нас нет такой специальности'
    return result


def check_fitness(student, profession):
    """

    :param student: получает номер студента для использвания функции get_student_by_pk
    :param profession: получает название профессии для использвания функции get_profession_by_title
    :return: возвращет словарь с данными имеющихся навыках, трбующихся, и проценте соотношения имеющихся и требуемых
    """

    profession_title = get_profession_by_title(profession)

    if isinstance(profession_title, str):
        return profession_title
    else:
        profession_skills = set(profession_title['skills'])

    student_pk = get_student_by_pk(student)

    if isinstance(student_pk, str):
        return student_pk
    else:
        student_skills = set(student_pk['skills'])

    has = list(profession_skills & student_skills)
    lacks = list(profession_skills - student_skills)
    percent = len(has) / len(profession_skills) * 100
    result = {'has': has, 'lacks': lacks, 'percent': percent}

    return result


