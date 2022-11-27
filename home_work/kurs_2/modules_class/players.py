class Plyer():

    def __init__(self, name):
        '''

        :param name: Имя игрока
        used_words - список используемых слов
        used_uncorrect_words - список ошибочных слов
        '''
        self.name = name
        self.used_uncorrect_words = []
        self.used_correct_words = []

    def len_correct_used_words(self):
        '''

        :return: количество правильных слов
        '''
        return len(self.used_correct_words)

    def len_uncorrect_used_words(self):
        '''

        :return: возвращает количество используемых слов
        '''
        return len(self.used_uncorrect_words)

    def is_used_word(self, word):
        '''

        :param word: проверяемое слово
        :return:  возвращает булево значение, было ли использовано слово
        '''
        result = False
        if word in self.used_uncorrect_words or word in self.used_correct_words:
            result = True
        return result

    def add_used_uncorrect_word(self, uncorrect_word):
        '''
        :param uncorrect_word: добавление в список неудачного слова
        '''
        if not self.is_used_word(uncorrect_word):
            self.used_uncorrect_words.append(uncorrect_word)

    def add_correct_used_word(self, correct_word):
        '''
        :param correct_word: добавление в список правильного слова
        '''
        if not self.is_used_word(correct_word):
            self.used_correct_words.append(correct_word)

    def __repr__(self):
        return 'Это экземпляр класса Plyer'
