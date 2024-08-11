from core.base_api import BaseAPI
from core.command import Command
import random


class Greet(BaseAPI):
    '''konnichiwa
    greetings: Write hello in different languages.
    greet [user]: Greets [user] in different language'''

    HELLO = ('sawatdee', 'barev', 'salam', 'cześć', 'wabula', 'salaam alaykum', 'hej', 'ndewo', 'namaskaram', 'helo', 'nyob zoo', 'geia sas', 'kamusta', 'marhaba', 'zdravo', 'zdraveĭte', 'ia ora na', 'muraho', 'yokwe', 'dumela', 'sveiki', 'namaste', 'bawo ni', 'sawubona', 'hai', 'hailo', 'sat sri akaal',
              'salam', 'kaixo', 'dumela', 'bok', 'szia', 'kuzu zangpo la', 'akkam', 'molo', 'merhaba', 'hei', 'xin chào', 'avuxeni', 'odi', 'živijo', 'konnichiwa', 'hello', 'hola', 'sabaidee', 'talofa', 'halo', 'gamardjoba', 'bula', 'ahoj', 'manao ahoana', 'salut', 'zdravstvuyte', 'olá', 'ciao', 'annyeonghaseyo',
              'kia ora', 'bonjour', 'halo', 'sannu', 'moni', 'moa oti', 'aloha', 'vitayu', 'mhoro', 'shalom', 'mālō e lelei', 'nǐ hǎo', 'ha lo', 'zdravo', 'habari', 'pronouncd nomoshkar', 'sain baina uu', 'hallo', 'chomreabsuor', 'tere', 'vanakkam', 'salemetsiz be', 'përshëndetje', 'salom', 'halló', 'greetings')

    def validate(self, cmd: Command) -> bool:
        return (
            cmd.command == 'greet' or
            cmd.command in self.HELLO or
            (cmd.is_command and not cmd.command)
        )

    def run(self, cmd: Command) -> None:
        if cmd.command == 'greet':
            user = cmd.author if cmd.param == 'me' else cmd.param
        elif not cmd.command:
            user = ''
        else:
            user = cmd.author
        return random.choice(self.HELLO) + ' ' + user
