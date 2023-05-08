from api import api_manager
from api.helper.message import Message


def api_test(msg):
    from api.gibberish import Gibberish
    api = Gibberish()

    if api.validate(msg):
        return api.run(msg)


def int_test(msg):
    return api_manager.execute(msg)


msg = Message.testInstance('vava encourage', 'user1')
# out = api_test(msg)
out = int_test(msg)
print(out)
