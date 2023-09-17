import discord
from discord.ext import commands

from utils import config

INITIAL_EXTENSIONS = ["cogs.members", "cogs.roles", "cogs.memo"]
PREFIX = ["!", "?", "/"]


class Bot(commands.Bot):
    async def setup_hook(self):
        print("Start setup_hook")
        for cog in INITIAL_EXTENSIONS:
            try:
                await self.load_extension(cog)
            except Exception as e:
                print(e)
        await self.tree.sync()
        print("End setup_hook")
        print("-" * 20)

    async def on_ready(self):
        print("Logged in as")
        for cog in INITIAL_EXTENSIONS:
            try:
                await self.reload_extension(cog)
            except Exception as e:
                print(e)

        await self.tree.sync()  # リロードしたコグを再同期する
        print(f"bot name: {self.user.name}")  # リロードの完遂を知らせる
        print(f"bot id: {self.user.id}")
        print("-" * 20)


intents = discord.Intents.all()
activity = discord.Activity(name="local", type=discord.ActivityType.competing)

bot = Bot(
    command_prefix=PREFIX,
    status=discord.Status.online,
    intents=intents,
    activity=activity,
)

# # エラー処理
# @bot.event
# async def on_command_error(ctx: commands.Context, error):
#     if ctx.author.bot:  # botが起こしたエラーなら
#         return  # 何もしない
#     if isinstance(error, commands.errors.CheckFailure):  # スラッシュコマンドでのみ動作するように制約
#         await ctx.send("勘の良いガキは嫌いだよ", ephemeral=True)  # 権限を持たずにコマンドを実行した際に警告する


if __name__ == "__main__":
    bot.run(config.TOKEN)
