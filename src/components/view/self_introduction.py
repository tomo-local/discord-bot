import discord
from discord.ext import commands

from components.modals.self_introduction import SelfIntroductionModal


class SelfIntroductionButton(discord.ui.View):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @discord.ui.button(label="OK", style=discord.ButtonStyle.success)
    async def gray_button(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_modal(SelfIntroductionModal(bot=self.bot))

    # @discord.ui.button(label="自己紹介 作成", style=discord.ButtonStyle.success)
    # async def create(self, button: discord.ui.Button, interaction: discord.Interaction):
    # await interaction.response.send_modal(SelfIntroductionModal(bot=self.bot))

    @discord.ui.button(label="自己紹介 更新", style=discord.ButtonStyle.gray)
    async def ng(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} NG")
