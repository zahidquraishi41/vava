from api import api_manager
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
        out = api_manager.execute(message)
        if out:
            await reply(out)
    except:
        with open('error.log', 'a') as f:
            f.write(str(dt.now()) + '\n')
            traceback.print_exc(file=f)
            f.write('\n\n')
        await reply(error.run(None))


keep_alive()
client.run(os.environ['VAVA_TOKEN'])
