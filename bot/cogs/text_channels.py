from discord.ext import commands


class TextChannelsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="text_channels", description="get text channel list")
    async def text_channels(self, ctx):
        text_channels = ctx.guild.text_channels
        text_channel_names = [text_channel.name for text_channel in text_channels]
        formatted_names = "\n".join([f"・{name}" for name in text_channel_names])
        await ctx.send(formatted_names)


async def setup(bot: commands.Bot):
    await bot.add_cog(TextChannelsCog(bot))
