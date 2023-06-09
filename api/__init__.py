from api.helper.api_manager import APIManager

from api.activate import Activate
from api.advice import Advice
from api.cat import Cat
from api.dad import Dad
from api.encourage import Encourage
from api.error import Error
from api.excuser import Excuser
from api.fact import Fact
from api.flirt import Flirt
from api.gibberish import Gibberish
from api.greet import Greet
from api.insult import Insult
from api.joke import Joke
from api.praise import Praise
from api.quote import Quote
from api.riddle import Riddle
from api.spam import Spam
from api.trivia import Trivia

api_manager = APIManager()

api_manager.register(Activate())
api_manager.register(Advice())
api_manager.register(Cat())
api_manager.register(Dad())
api_manager.register(Encourage())
api_manager.register(Error())
api_manager.register(Excuser())
api_manager.register(Fact())
api_manager.register(Flirt())
api_manager.register(Gibberish())
api_manager.register(Greet())
api_manager.register(Insult())
api_manager.register(Joke())
api_manager.register(Praise())
api_manager.register(Quote())
api_manager.register(Riddle())
api_manager.register(Spam())
api_manager.register(Trivia())
