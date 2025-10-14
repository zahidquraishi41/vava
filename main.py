import discord as dc
from api_handler import APIHandler
import os
from dotenv import load_dotenv
import asyncio

intents = dc.Intents.default()
intents.message_content = True
client = dc.Client(intents=intents)
manager = APIHandler()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: dc.Message):
    if message.author == client.user:
        return

    reply = message.channel.send
    out = None
    try:
        out = manager.process(message)
        if out:
            if isinstance(out, list):
                for item in out:
                    await reply(item)
                    await asyncio.sleep(1)  # 1-second delay
            else:
                await reply(out)
    except KeyboardInterrupt:
        return
    except Exception as e:
        out = e
        await reply(str(e))
    finally:
        if out:
            print(f"In: {message.content} | Out: {out} | By: {message.author.name}")


load_dotenv()
client.run(os.getenv("VAVA_TOKEN"))
