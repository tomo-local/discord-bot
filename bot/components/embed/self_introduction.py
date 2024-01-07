import discord
from discord.ext.commands import Bot

from discord.ui import TextInput
from discord import Embed, Interaction


class SelfIntroductionEmbed(Embed):
    def __init__(
        self,
        detail: TextInput,
        java_id: TextInput,
        bedrock_id: TextInput,
        bot: Bot,
        interaction: Interaction,
    ):
        super().__init__()

        self.set_author(
            icon_url=interaction.user.avatar.url,
            name=f"{interaction.user.display_name} ({interaction.user})",
        )
        self.set_footer(
            icon_url=bot.user.avatar.url,
            text=bot.user.display_name,
        )

        self.description = detail.value
        self.color = discord.Color.random()

        if java_id.value:
            self.add_field(
                name="java id",
                value=java_id.value,
                inline=True,
            )

        if bedrock_id.value:
            self.add_field(
                name="bedrock id",
                value=bedrock_id.value,
            )
