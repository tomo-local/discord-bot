import discord
from discord.ext import commands
from discord import Interaction, ui, SelectOption

from components.view.self_introduction import SelfIntroductionButton
from components.modals.self_introduction import SelfIntroductionModal


class SampleViewA(ui.View):
    def __init__(self, bot: commands.Bot):
        super().__init__(timeout=180)
        self.bot = bot

    @discord.ui.select(
        cls=ui.Select,
        placeholder="What is your favorite fruit?",
        options=[
            SelectOption(label="自己紹介", value="自己紹介"),
            SelectOption(label="test", value="test"),
            SelectOption(label="a", value="aaa"),
        ],
    )
    async def select(self, interaction: Interaction, select: ui.Select):
        print(select.values[0])

        if select.values[0] == "自己紹介":
            await interaction.response.send_modal(SelfIntroductionModal(bot=self.bot))
        else:
            await interaction.response.send_message(
                f"{interaction.user.mention} {select.values[0]}"
            )


class ConfigCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name="update_config", hidden=True)
    @commands.is_owner()
    async def update_config(self, ctx: commands.Context):
        await ctx.send(view=SampleViewA(bot=self.bot), ephemeral=True)

    @commands.hybrid_command(name="set_button", hidden=True)
    @commands.is_owner()
    async def set_button(self, ctx: commands.Context):
        await ctx.send(view=SelfIntroductionButton(bot=self.bot))


async def setup(bot: commands.Bot):
    await bot.add_cog(ConfigCog(bot))
