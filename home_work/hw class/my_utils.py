class Question():

    def __init__(self, title_quest, complexity_quest, correct_answer):
        """

        :param title_quest: текст вопроса
        :param complexity_quest: сложность вопроса
        :param correct_answer: правильный ответ
        question_asked: есть ли правильный ответ от пользователя
        answer_user: ответ пользователя
        score_quest - количество балов за данный вопрос
        """

        self.title_quest = title_quest
        self.complexity_quest = int(complexity_quest)
        self.correct_answer = str(correct_answer)
        self.question_asked = False
        self.answer_user = None
        self.score_quest = 0

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        self.score_quest = self.complexity_quest * 10
        return self.score_quest

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        if str(self.answer_user).lower() == self.correct_answer.lower():
            self.question_asked = True

        return self.question_asked

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        result = f'Вопрос: {self.title_quest}\nСложность {self.complexity_quest}/5'

        return result

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """

        result = f'Ответ верный, получено {self.score_quest} баллов'

        return result

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        result = f'Ответ неверный, верный ответ {self.correct_answer}'

        return result
