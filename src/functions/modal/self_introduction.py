import discord
import random

from discord.ui import Modal


class SelfIntroductionModal(Modal, title="Self-Introduction"):
    self_introduction = discord.ui.TextInput(
        label="自己紹介",
        custom_id="self_introduction",
        placeholder="例）\n【年齢】20歳 \n【趣味】ゲーム \n【性別】男\n",
        style=discord.TextStyle.paragraph,
    )

    java_id = discord.ui.TextInput(
        label="Minecraft Java Id", placeholder="Your java minecraft id", required=False
    )

    bedrock_id = discord.ui.TextInput(
        label="Minecraft Bedrock Id",
        placeholder="Your bedrock minecraft id",
        required=False,
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            color=discord.Color.random(), description=self.self_introduction.value
        )
        embed.set_author(
            icon_url=interaction.user.avatar.url, name=interaction.user.display_name
        )

        if self.java_id.value:
            embed.add_field(
                name="java id",
                value=self.java_id.value,
                inline=True,
            )

        if self.bedrock_id.value:
            embed.add_field(
                name="java id",
                value=self.java_id.value,
            )

        await interaction.response.send_message(embed=embed)
