''' DON'T REMOVE/MODIFY COMMENTS'''
# helper imports
from api.helper.api_manager import APIManager

# api imports
from api.greet import Greet


# api manager init
api_manager = APIManager()

# api manager register
api_manager.register(Greet())
