import discord

from utils import config
from functions import message as fun_message


intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("-" * 20)
    print("login discord")
    print("-" * 20)
    print("ログインしました")


@client.event
async def on_raw_typing(payload):
    print("typing just now")
    print("-" * 20)
    print(payload)
    return


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        await fun_message.reply(message)

    print(fun_message.get_data(message))


if __name__ == "__main__":
    client.run(config.TOKEN)
