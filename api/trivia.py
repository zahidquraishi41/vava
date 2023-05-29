from api.helper.api_base import APIBase
from api.helper.message import Message
from api.helper.utils import fetch
import requests


class Trivia(APIBase):
    def __init__(self) -> None:
        super().__init__()
        self.answer = ''
        self.difficulty = 'easy'

    def validate(self, msg: Message):
        return msg.command in (
            'trivia', 'trivia easy',
            'trivia medium', 'trivia hard'
        ) or \
            (self.answer and msg.content == self.answer)

    def run(self,  msg: Message):
        if not msg.command:
            self.answer = ''
            return 'Correct!'

        if ' ' in msg.command:
            self.difficulty = msg.command.split(' ', 1)[1]

        return self.fetch_trivia()

    def help(self) -> dict:
        return {
            'trivia': 'Asks trivia question from films, food_and_drink, general_knowledge, geography, science',
            'trivia easy': 'Sets the difficulty to easy',
            'trivia medium': 'Sets the difficulty to medium',
            'trivia hard': 'Sets the difficulty to hard'
        }

    def fetch_trivia(self):
        url = f'https://the-trivia-api.com/api/questions?categories=film_and_tv,food_and_drink,general_knowledge,geography,science&limit=20&difficulty={self.difficulty}'

        if not self.buffer:
            self.buffer = fetch(url)
        if self.difficulty not in [trivia['difficulty'] for trivia in self.buffer]:
            self.buffer.extend(fetch(url))

        for trivia in self.buffer:
            if trivia['difficulty'] == self.difficulty:
                question = self.prepare_trivia(trivia)
                self.buffer.remove(trivia)
                return question

    def prepare_trivia(self, trivia):
        choices = trivia['incorrectAnswers'] + [trivia['correctAnswer']]
        random.shuffle(choices)
        self.answer = choices.index(trivia['correctAnswer'])
        map = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
        self.answer = map[self.answer]

        choices_str = ''
        for i, e in enumerate(list(map.values())):
            choices_str += e + '. ' + choices[i] + '\n'
        return trivia['question'] + '\n' + choices_str
