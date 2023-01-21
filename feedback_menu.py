import discord
from feedback_modal import Feedback


class ReportMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Отчет об ошибке', style=discord.ButtonStyle.red)
    async def send_report(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(Feedback())

