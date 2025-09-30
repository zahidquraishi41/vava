import discord as dc
from api_handler import APIHandler
import os
from flask_app import keep_alive
from dotenv import load_dotenv

intents = dc.Intents.default()
intents.message_content = True
client = dc.Client(intents=intents)
manager = APIHandler()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: dc.Message):
    if message.author == client.user:
        return

    reply = message.channel.send
    try:
        out = manager.process(message)
        if out:
            await reply(out)
    except KeyboardInterrupt:
        return
    except Exception as e:
        await reply(e)

load_dotenv()
keep_alive()
client.run(os.getenv('VAVA_TOKEN'))