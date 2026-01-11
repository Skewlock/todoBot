import discord

class TaskView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(style=discord.ButtonStyle.green, label="Task done !", custom_id="todo:check")
    async def taskDone(self, interaction: discord.Interaction, button: discord.ui.Button):
        print("AAAAAAAAAAAAAAAAAAAAAAAA")
        await interaction.response.send_message('Task marked as success !', ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.red, label="Task canceled !", custom_id="todo:failed")
    async def taskFailed(self, interaction: discord.Interaction, Button: discord.ui.Button):
        print("BBBBBBBBBBBBBBBBBBBBBBBBBB")
        await interaction.response.send_message('Task marked as failed', ephemeral=True)