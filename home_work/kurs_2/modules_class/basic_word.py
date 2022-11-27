class BasicWord():

    def __init__(self, initial_word, valid_words):
        '''

        :param initial_word: Исходное слово
        :param valid_words: Список слов которые можно составить из исходного слова
        '''
        self.initial_word = initial_word
        self.valid_words = valid_words

    def is_valid_word(self, word):
        '''

        :param word: слово которое вводит пользователь
        :return: возвращает есть ли слово в списке допустимых
        '''
        result = False
        if word in self.valid_words:
            result = True
        return result

    def count_valid_words(self):
        '''

        :return: возвращает количество допустимых слов
        '''
        return len(self.valid_words)

    def min_litter(self):
        '''
        :return: возвращает минимальное количество символов в допустимых словах
        '''
        word = min(self.valid_words, key=len)
        return len(word)

    def max_litter(self):
        '''

        :return: возвращает минимальное количество символов в допустимых словах
        '''
        word = max(self.valid_words, key=len)
        return len(word)

    def __repr__(self):
        return 'Это экземпляр класса BasicWord'
