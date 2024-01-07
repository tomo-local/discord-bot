import discord

from discord.ui import Modal

from discord.ui import TextInput
from discord import Embed, Interaction
from discord.ext import commands
from discord.ext.commands import Bot


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
