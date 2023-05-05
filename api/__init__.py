from api.helper.api_manager import APIManager

from api.greet import Greet

api_manager = APIManager()

api_manager.register(Greet())
