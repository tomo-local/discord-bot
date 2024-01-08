from discord import Embed, Member, Role, Color
from discord.ext import commands
from discord.utils import get


class RoleCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_member_join(
        self,
        member: Member,
    ):
        if member.bot:
            role = get(member.guild.roles, name="bot")
        else:
            role = get(member.guild.roles, name="member")

        await member.add_roles(role)

    @commands.hybrid_command(name="set_role", description="on role")
    async def set_role(
        self,
        ctx: commands.Context,
        member: Member,
        role: Role,
    ):
        if role in member.roles:
            embed = Embed(
                description=f"{member.mention} に {role.mention} 役職はすでに付与されています。",
                color=Color.blue(),
            )
            await ctx.send(embed=embed)
            return

        try:
            await member.add_roles(role)
            embed = Embed(
                description=f"{member.mention} に {role.mention} 役職が付与されました。",
                color=Color.green(),
            )
        except Exception as e:
            print(e)
            embed = Embed(
                description=f"{member.mention} に　{role.mention} 役職を付与することはできません。",
                color=Color.red(),
            )

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(RoleCog(bot))
