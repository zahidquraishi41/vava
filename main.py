from api import api_manager
from api.helper.message import Message
from api.error import Error
import discord as dc
from datetime import datetime as dt
from flask_app import keep_alive
import os
import traceback

intents = dc.Intents.default()
intents.message_content = True
client = dc.Client(intents=intents)
error = Error()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    reply = message.channel.send

    try:
        msg = Message(message)
        out = api_manager.execute(msg)
        if out:
            await reply(out)
    except Exception as e:
        print('\n')
        print(dt.now())
        print(e)
        print('User command: ', message.content)
        print('\n')
        await reply(error.run(None))


keep_alive()
client.run(os.environ['VAVA_TOKEN'])
