from api.helper.api_manager import APIManager

from api.encourage import Encourage
from api.error import Error
from api.gibberish import Gibberish
from api.greet import Greet
from api.joke import Joke

api_manager = APIManager()

api_manager.register(Encourage())
api_manager.register(Error())
api_manager.register(Gibberish())
api_manager.register(Greet())
api_manager.register(Joke())
