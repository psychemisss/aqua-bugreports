import discord
import traceback
from integrations.notion_api import NotionAPI


class Feedback(discord.ui.Modal, title='Отчет об ошибке'):
    notion_client = NotionAPI()

    problem = discord.ui.TextInput(
        label='Опишите проблему',
        style=discord.TextStyle.long,
        placeholder='Опишите баг или проблему, которую вы встретили...',
        required=True
    )

    feedback = discord.ui.TextInput(
        label='Шаги воспроизведения',
        style=discord.TextStyle.long,
        placeholder='Опишите действия предшествующие возникновению данного бага/проблемы...',
        required=True,
        max_length=300,
    )

    attachments = discord.ui.TextInput(
        label='Дополнительные сведения (необязательно)',
        style=discord.TextStyle.long,
        placeholder='Приложите ссылки на скриншоты или видео, на которых можно увидеть баг/проблему...',
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Спасибо за помощь в нахождении этого бага, ' +
                                                'в ближайшее время мы разберемся с ним, приятной игры!',
                                                ephemeral=True)

        # send data to notion
        self.notion_client.create_report(
            f"{self.problem.value}  [{interaction.user}]",
            self.feedback.value,
            self.attachments.value
        )

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)


class ReportMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Отчет об ошибке', style=discord.ButtonStyle.red)
    async def send_report(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(Feedback())
