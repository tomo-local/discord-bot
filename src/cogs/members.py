from discord.ext import commands


class MembersCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot: commands.Bot = bot

    @commands.command(name="members", description="get member list")
    async def members(self, ctx):
        members = ctx.guild.members

        member_names = [member.name for member in members]

        formatted_names = "\n".join([f"・{name}" for name in member_names])

        await ctx.send(f"{formatted_names}")

    @commands.command(name="test", description="test")
    async def test(self, ctx):
        print("test")
        await ctx.send("test")


async def setup(bot: commands.Bot):
    await bot.add_cog(MembersCog(bot))
