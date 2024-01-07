from discord.ext import commands
from .modal import MemoModal


class MemoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name="memo", description="You want to create the memo")
    async def memo(self, ctx: commands.Context):
        modal = MemoModal(bot=self.bot)
        await ctx.interaction.response.send_modal(modal)


async def setup(bot: commands.Bot):
    await bot.add_cog(MemoCog(bot))
