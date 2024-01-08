from bot import Bot
from bot.core.utils import config

import discord

intents = discord.Intents.all()
activity = discord.Activity(name="local", type=discord.ActivityType.competing)

bot = Bot(
    command_prefix=config.PREFIX,
    status=discord.Status.online,
    intents=intents,
    activity=activity,
)

if __name__ == "__main__":
    bot.run(config.TOKEN)
