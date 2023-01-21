import discord
from discord import app_commands

from feedback_modal import Feedback
from feedback_menu import ReportMenu

# The guild in which this slash command will be registered.
# It is recommended to have a test guild to separate from your "production" bot
TEST_GUILD = discord.Object(GUILD_ID)


class MyClient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def setup_hook(self) -> None:
        # Sync the application command with Discord.
        await self.tree.sync(guild=TEST_GUILD)


client = MyClient()


@client.tree.command(guild=TEST_GUILD, description="Submit feedback")
async def feedback(interaction: discord.Interaction):
    # Send the modal with an instance of our `Feedback` class
    # Since modals require an interaction, they cannot be done as a response to a text command.
    # They can only be done as a response to either an application command or a button press.
    await interaction.response.send_modal(Feedback())


@client.tree.command(guild=TEST_GUILD, description="Send report menu to a channel")
async def report(interaction: discord.Interaction):
    embed = discord.Embed(title='Отчет об ошибке',
                          description='Вы можете отправить отчет об ошибке, нажав на кнопку ниже',
                          color=discord.Color.red())
    await interaction.response.send_message(embed=embed, view=ReportMenu())


client.run(TOKEN)