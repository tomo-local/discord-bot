from discord import Embed, Member, Role, Color, Forbidden
from discord.ext import commands
from discord.utils import get


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def _set_role(
        self, ctx: commands.Context, member: Member, role: Role, *, check_user=True
    ):
        if member.get_role(role.id) is not None:
            await ctx.send(
                embed=Embed(
                    description=f"{member.mention} に {role.mention} 役職はすでに付与されています。",
                    color=Color.blue(),
                )
            )
            return

        try:
            await member.add_roles(role)
        except Forbidden:
            await ctx.send(
                embed=Embed(
                    description=f"{member.mention} に {role.mention} 役職を付与することはできません。",
                    color=Color.red(),
                )
            )
        else:
            await ctx.send(
                embed=Embed(
                    description=f"{member.mention} に {role.mention} 役職が付与されました。",
                    color=Color.green(),
                )
            )

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
        await self._set_role(ctx, member, role)


async def setup(bot) -> None:
    await bot.add_cog(Roles(bot))
