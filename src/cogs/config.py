import discord
from discord.ext import commands


class HogeList(discord.ui.View):
    def __init__(self, args):
        super().__init__()
        self.add_item(HugaList(args))


class HugaList(discord.ui.Select):
    def __init__(self, args):
        options = []
        for item in args:
            options.append(discord.SelectOption(label=item, description=""))

        super().__init__(placeholder="", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"{interaction.user.name}は{self.values[0]}を選択しました"
        )


class ConfigCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name="update_config", hidden=True)
    @commands.is_owner()
    async def update_config(self, ctx: commands.Context, *args):
        await ctx.send(view=HogeList(args))


async def setup(bot: commands.Bot):
    await bot.add_cog(ConfigCog(bot))
