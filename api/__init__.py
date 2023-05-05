from api.helper.api_manager import APIManager

from api.joke import Joke
from api.greet import Greet

api_manager = APIManager()

api_manager.register(Joke())
api_manager.register(Greet())
