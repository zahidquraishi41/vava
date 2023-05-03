from api import api_manager
from api.helper.message import Message

msg = Message.testInstance('vava', 'user1')

out = api_manager.execute(msg)
print(out)
