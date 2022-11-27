# импорты

import requests
import random
from modules_class.basic_word import *


# получение данных с jsonkeeper

def jsonkeeper():
    json_data_req = requests.get("https://www.jsonkeeper.com/b/I101")
    result = json_data_req.json()
    return result


# получение случайного набора данных


def load_random_word():
    word_and_list_valid_words = jsonkeeper()
    random_word = random.choice(word_and_list_valid_words)
    basic_word = BasicWord(random_word['word'], random_word['subwords'])
    return basic_word
