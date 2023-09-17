import discord
import datetime

from discord.ui import Modal


class MemoModal(Modal, title="Memo"):
    name = discord.ui.TextInput(
        label="Title", custom_id="memo_title", placeholder="Your Memo title"
    )

    details = discord.ui.TextInput(
        label="Memo",
        custom_id="memo_details",
        style=discord.TextStyle.paragraph,
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(description=self.details.value)
        embed.set_author(icon_url=interaction.user.avatar.url, name=self.name.value)
        dt_now = datetime.datetime.now()
        now = dt_now.strftime("%Y/%m/%d")

        embed.set_footer(text=f"time:{now}  creater: {interaction.user.display_name}")

        await interaction.response.send_message(embed=embed)
