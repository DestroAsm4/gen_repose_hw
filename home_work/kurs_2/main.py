# импорты, класс basic_word вызывается вместе с utils

from utils import *
from modules_class.players import *

# Ввод имени

name = input('Введите имя игрока: ').strip()

# получение экземпляров классов Player и Basice_word, получение мин и макс от Basice_word

player = Plyer(name)
basic_word = load_random_word()
min_litter = basic_word.min_litter()
max_litter = basic_word.max_litter()

# Приветствие

print(f'Привет, {name}')
print(f'Составте {basic_word.count_valid_words()} слов из слова "{basic_word.initial_word}"')
print(f'Слова должны быть не короче {min_litter} букв, и не больше {max_litter} букв')
print(f'Чтобы закончить игру, угадайте все слова или напишите "stop"')
print(f'Поехали, ваше первое слово?')

# цикл для угадывания слов

while player.len_correct_used_words() != basic_word.count_valid_words():
    word = input()
    # если было написано "стоп"
    if word.lower() == 'стоп' or word.lower() == 'stop':
        break
    elif min_litter > len(word) or len(word) > max_litter:
        # проверка количества символов
        print('Количество символов не соответствует требуемому')
        player.add_used_uncorrect_word(word.lower())
        continue
    elif player.is_used_word(word.lower()):
        # проверка случая повтора слова
        print('Слово уже было')
        player.add_used_uncorrect_word(word.lower())
        continue
    elif word.lower() not in basic_word.valid_words:
        # обработка неудачного слова
        print('Слово не удачное')
        player.add_used_uncorrect_word(word.lower())
        continue
    elif basic_word.is_valid_word(word.lower()):
        # обработка веррного ответа
        if basic_word.count_valid_words() - player.len_correct_used_words() - 1 != 0:
            print(f'Верно, еще {basic_word.count_valid_words() - player.len_correct_used_words() - 1} слов')
            player.add_correct_used_word(word.lower())
        else:
            print(f'Верно')
            player.add_correct_used_word(word.lower())

# вывод итогов

print(f'Игра завершена вы угадали {player.len_correct_used_words()} слов!')
print(f'Вы совершили {player.len_uncorrect_used_words()} ошибок')
