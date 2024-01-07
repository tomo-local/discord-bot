import discord
from discord.ui import Modal
from discord.ext import commands

from .embed import MemoEmbed


class MemoModal(Modal, title="Memo"):
    # TODO: fieldの各パラメータをi18nに対応させる
    name = discord.ui.TextInput(
        label="Title", custom_id="memo_title", placeholder="Your Memo title"
    )

    detail = discord.ui.TextInput(
        label="Memo",
        custom_id="memo_details",
        style=discord.TextStyle.paragraph,
    )

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot: commands.Bot = bot

    async def on_submit(self, interaction: discord.Interaction):
        embed = MemoEmbed(
            modal=self,
            bot=self.bot,
            interaction=interaction,
        )

        await interaction.response.send_message(embed=embed)
