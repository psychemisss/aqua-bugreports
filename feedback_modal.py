import discord
import traceback


class Feedback(discord.ui.Modal, title='Отчет об ошибке'):
    name = discord.ui.TextInput(
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
        await interaction.response.send_message(f'Спасибо за помощь в нахождении этого бага,' +
                                                'в ближайшее время мы разберемся с ним, приятной игры!',
                                                ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
