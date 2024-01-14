import discord
from discord.ext import commands

INITIAL_EXTENSIONS = [
    "bot.cogs.admin.admin",
    "bot.cogs.admin.roles",
    "bot.cogs.channels.text_channels",
    "bot.cogs.config.config",
    "bot.cogs.members.members",
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
                print(cog)
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