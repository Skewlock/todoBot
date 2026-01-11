import discord

class TaskView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(style=discord.ButtonStyle.green, label="Finish task", custom_id="todo:check")
    async def taskDone(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Task marked as success !', ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="Repoen task", custom_id="todo:reopened")
    async def taskReopened(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message('Task reopened', ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.red, label="Cancel task", custom_id="todo:failed")
    async def taskFailed(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await interaction.response.send_message('Task marked as failed', ephemeral=True)