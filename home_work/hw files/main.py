# Импорты

import os
import random

# Переменные
ADRESS_TXT_FILES = {'history': 'history.txt', 'words': 'words.txt'}

SCORE = 0

# Приветствие и получение имени

while True:
    data_user_name = input('Представьтесь пожалуйста: ')
    if data_user_name in ':':
        print('Нельзя использовать символы - ":"')
        data_user_name = input('Представьтесь пожалуйста: ')
    else:
        break


# Функция для оздания списка слов


def read_file_words(adress_words):
    '''
    :param adress_words: адресс файла со списком слов для создания вопросов
    :return: выводит список слов в формате list()
    '''

    words = []

    with open(os.path.join(adress_words), 'rt', encoding='utf-8') as file_words:
        for word in file_words:
            words.append(word.strip())
    return words

# Функция для записи истории игр


def write_file_history(adress_history_file, score):
    '''
    :param adress_history_file: Адресс файла истории
    :return: возвращаемого значения нет, происходит запись в файл по введенному адрессу
    '''

    with open(os.path.join(adress_history_file), 'a', encoding='utf-8') as history_file:
        history_file.write(data_user_name + ': ' + str(score) + '\n')

# Функция для чтения истории и вывода общих результатов игр


def read_file_history(adress_history_file, name_player):
    '''

    :param adress_history_file: адресс файла истории игры
    :param name_player: имя игрока
    :return: выводит сумму игр и лучший результат в виде текста
    '''
    result_text = ''
    al_play = 0
    max_score = 0
    file_empty = False

    with open(os.path.join(adress_history_file), 'rt', encoding='utf-8') as history_file:
        for read_line in history_file:
            if read_line == '':
                file_empty = True
                break

            if len(read_line.split(': ')) > 1:
                name, score = read_line.split(': ')

            else:
                print("ошибка")
            if name_player == name:
                al_play += 1
                if int(score) > max_score:
                    max_score = int(score)
        if not file_empty:
            result_text += f'Всего игр {str(al_play)}\nЛучший результат {str(max_score)}'
        else:
            result_text = 'История пуста'

    return result_text

# Список слов

words = read_file_words(ADRESS_TXT_FILES['words'])

# Цикл вопросов

for word in words:
    quest = list(word)
    random.shuffle(quest)
    quest = ''.join(quest)
    answer = input(f'\nУгадайте слово: {quest}\n')

    if answer.lower() == word.lower():
        print('Верно, вы получаете 10 очков\n')
        SCORE += 10
    else:
        print(f'Неправильно, правильный ответ - {word}\n')

# Вывод\запись результатов данной игры, и вывод результатов всех игр данного игрока

print(f'{data_user_name}\nВаш результат {SCORE}')
write_file_history(ADRESS_TXT_FILES['history'], SCORE)
print(read_file_history(ADRESS_TXT_FILES['history'], data_user_name))