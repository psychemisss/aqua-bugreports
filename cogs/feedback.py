import discord
import traceback

from integrations.notion_api import NotionAPI
from helpers.config_manager import load_config_variable


class Feedback(discord.ui.Modal, title=load_config_variable("FEEDBACK_MODAL", "MODAL_TITLE")):
    notion_client = NotionAPI()

    problem = discord.ui.TextInput(
        label=load_config_variable("FEEDBACK_MODAL", "FIRST_FIELD_TITLE"),
        style=discord.TextStyle.long,
        placeholder=load_config_variable("FEEDBACK_MODAL", "FIRST_FIELD_PLACEHOLDER"),
        required=load_config_variable("FEEDBACK_MODAL", "FIRST_FIELD_REQUIRED"),
    )

    feedback = discord.ui.TextInput(
        label=load_config_variable("FEEDBACK_MODAL", "SECOND_FIELD_TITLE"),
        style=discord.TextStyle.long,
        placeholder=load_config_variable("FEEDBACK_MODAL", "SECOND_FIELD_PLACEHOLDER"),
        required=load_config_variable("FEEDBACK_MODAL", "SECOND_FIELD_REQUIRED"),
    )

    attachments = discord.ui.TextInput(
        label=load_config_variable("FEEDBACK_MODAL", "THIRD_FIELD_TITLE"),
        style=discord.TextStyle.long,
        placeholder=load_config_variable("FEEDBACK_MODAL", "THIRD_FIELD_PLACEHOLDER"),
        required=load_config_variable("FEEDBACK_MODAL", "THIRD_FIELD_REQUIRED"),
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            load_config_variable("FEEDBACK_MODAL", "SUCCESS_MESSAGE"),
            ephemeral=True
        )

        # send data to notion
        self.notion_client.create_report(
            f"{self.problem.value} [{interaction.user}]",
            self.feedback.value,
            self.attachments.value
        )

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(
            load_config_variable("FEEDBACK_MODAL", "ERROR_MESSAGE"),
            ephemeral=True
        )

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)


class ReportMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label=load_config_variable("FEEDBACK_MENU", "MENU_BUTTON"), style=discord.ButtonStyle.red)
    async def send_report(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(Feedback())
