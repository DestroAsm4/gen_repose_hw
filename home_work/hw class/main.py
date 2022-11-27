from my_utils import *
import json
import os
import random

score = 0
count_correct_answer = 0


def make_list_questions(link):
    """
    link: ссылка на json файл со списком вопросов где q - вопрос, d - сложность вопроса
    a - отавет на вопрос
    Работает на основе модуля questionclass, используя файл questions.json
    создает список экземпляров класса Question
    :return: создает список экземпляров класса Question

    """

    object_questions_list = []

    with open(os.path.join(link), 'rt', encoding='utf-8') as questions_file:
        questions_list = json.load(questions_file)

    for quest in questions_list:
        object_questions_list.append(Question(quest['q'], quest['d'], quest['a']))
    return object_questions_list


def final_results(count_correct_answer, len_questions, score):
    """

    :param count_correct_answer: количество правильных ответов
    :param len_questions: всего вопросов
    :param score: всего набрано баллов
    :return: текст итогов
    """
    result = f'Вот и все!\n' \
             f'Отвечено {count_correct_answer} вопроса из {len_questions}\n' \
             f'Набрано {score} баллов'
    return result


# вызов функции для создания списка вопросов и создание переменной len_questions: количество вопросов

questions = make_list_questions('questions.json')
len_questions = len(questions)

print('Игра начинается!')

# перемешивание вопросов

random.shuffle(questions)

# цикл вопросов
for quest in questions:

    # выдача вопроса
    print(quest.build_question())

    # Получение ответа
    quest.answer_user = input()

    # если ответ верен то прибавляется кол верных ответов и балов, выдается информация о положительном результате
    if quest.is_correct():
        score += quest.get_points()
        count_correct_answer += 1
        print(quest.build_positive_feedback())
    else:

        # выдача отрицательного результата

        print(quest.build_negative_feedback())

# выдача итогов
print(final_results(count_correct_answer, len_questions, score))
