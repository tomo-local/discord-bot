import discord
from discord.ext import commands

from utils import config

INITIAL_EXTENSIONS = [
    "cogs.owner",
    # "cogs.config",
    "cogs.members",
    "cogs.roles",
    "cogs.memo",
]
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

    async def on_guild_join(self, guild: discord.Guild):
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(
                read_messages=True, send_messages=False
            ),
        }

        setting_channel = guild.get_channel("local-config")

        if setting_channel == None:
            channel: discord.TextChannel = await guild.create_text_channel(
                name="local-config", overwrites=overwrites
            )
        else:
            await setting_channel.set_permissions(overwrites=overwrites)
            channel = setting_channel

        embed = discord.Embed(
            title="local bot setting",
            color=discord.Color.green(),
            description="これはLocal bot設定のチャンネルになります。\n このチャンネル,メッセージを削除しないでください。",
        )

        embed.add_field(
            name="self introduction channel", value="Not setting", inline=False
        )
        embed.add_field(name="memo channel", value="Not setting", inline=False)
        embed.add_field(name="default member role", value="Not setting", inline=False)
        embed.add_field(name="default bot role", value="Not setting", inline=False)

        await channel.send(embed=embed)


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
