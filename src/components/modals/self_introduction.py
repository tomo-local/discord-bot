import discord

from discord.ui import Modal
from discord.ext import commands

from components.embed.self_introduction import SelfIntroductionEmbed


class SelfIntroductionModal(Modal, title="Self-Introduction"):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot: commands.Bot = bot

    self_introduction = discord.ui.TextInput(
        label="自己紹介",
        custom_id="self_introduction",
        placeholder="例）\n【年齢】20歳 \n【趣味】ゲーム \n【性別】男\n",
        style=discord.TextStyle.paragraph,
    )

    java_id = discord.ui.TextInput(
        label="Java Id", placeholder="Your java minecraft id", required=False
    )

    bedrock_id = discord.ui.TextInput(
        label="Bedrock Id",
        placeholder="Your bedrock minecraft id",
        required=False,
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = SelfIntroductionEmbed(
            detail=self.self_introduction,
            java_id=self.java_id,
            bedrock_id=self.bedrock_id,
            bot=self.bot,
            interaction=interaction,
        )

        channel = self.bot.get_channel(1153134310631673927)

        await channel.send(embed=embed)

        await interaction.response.send_message(embed=embed, ephemeral=True)
