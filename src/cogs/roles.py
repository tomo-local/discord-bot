import discord
from discord.ext import commands


class RoleCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            role = discord.utils.get(member.guild.roles, name="bot")
        else:
            role = discord.utils.get(member.guild.roles, name="member")

        await member.add_roles(role)

    @commands.hybrid_command(name="set_role", description="on role")
    async def set_role(self, ctx, member: discord.Member, role: discord.Role):
        if role in member.roles:
            embed = discord.Embed(
                description=f"{member.mention} に {role.mention} 役職はすでに付与されています。",
                color=discord.Color.blue(),
            )
            await ctx.send(embed=embed)
            return

        try:
            await member.add_roles(role)
            embed = discord.Embed(
                description=f"{member.mention} に {role.mention} 役職が付与されました。",
                color=discord.Color.green(),
            )
        except Exception as e:
            print(e)
            embed = discord.Embed(
                description=f"{member.mention} に　{role.mention} 役職を付与することはできません。",
                color=discord.Color.red(),
            )

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(RoleCog(bot))
