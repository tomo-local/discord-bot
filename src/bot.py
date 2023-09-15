import discord
from discord.ext import commands

from utils import config

INITIAL_EXTENSIONS = [
    "cogs.members",
]
prefix = ["!", "?", "/"]  # list型で複数の接頭辞に対応


class Bot(commands.Bot):
    async def setup_hook(self):
        for cog in INITIAL_EXTENSIONS:
            try:
                await self.load_extension(cog)
            except Exception as e:
                print(e)
        await self.tree.sync()

    async def on_ready(self):
        print("Logged in as")
        for cog in INITIAL_EXTENSIONS:
            try:
                await self.reload_extension(cog)
            except Exception as e:
                print(e)

        await self.tree.sync()  # リロードしたコグを再同期する
        print(self.user.name)  # リロードの完遂を知らせる
        print(self.user.id)
        print("------")


intents = discord.Intents.all()
activity = discord.Activity(name="local", type=discord.ActivityType.competing)

bot = Bot(
    command_prefix=prefix,
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
