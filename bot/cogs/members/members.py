from discord import Embed, Color
from discord.ext import commands

from components.modals.self_introduction import SelfIntroductionModal


class MembersCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name="self_introduction", description="self-introduction")
    async def self_introduction(self, ctx: commands.Context):
        modal = SelfIntroductionModal(bot=self.bot)
        await ctx.interaction.response.send_modal(modal)

    @commands.hybrid_command(name="members", description="get member list")
    async def members(self, ctx: commands.Context, name: str = None):
        members = ctx.guild.members
        embed = Embed(title="Member List", color=Color.blue())

        if name:
            filtered_members = [
                member for member in members if name.lower() in member.name.lower()
            ]
        else:
            filtered_members = members

        for member in filtered_members:
            member_name = member.name
            member_display_name = (
                member.display_name if member.display_name else member_name
            )
            member_roles = ", ".join([role.name for role in member.roles])
            embed.add_field(
                name=f"{member_display_name} ({member_name})",
                value=member_roles,
                inline=False,
            )

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(MembersCog(bot))
