import discord
from discord.ext.commands import Bot
from discord.ui import Modal

from discord import Embed, Interaction


class MemoEmbed(Embed):
    def __init__(
        self,
        modal: Modal,
        bot: Bot,
        interaction: Interaction,
    ):
        super().__init__()
        self.bot = bot
        self.interaction = interaction

        self.title = modal.name.value
        self.description = modal.detail.value
        self.color = discord.Color.light_gray()

        self.set_author(
            icon_url=interaction.user.avatar.url,
            name=f"{interaction.user.display_name} ({interaction.user})",
        )
        self.set_footer(
            icon_url=bot.user.avatar.url,
            text=bot.user.display_name,
        )
