import discord

class TaskView(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(style=discord.ButtonStyle.green, label="Task done !")
    async def taskDone(interaction: discord.Interaction, button: discord.ui.Button):
        print("AAAAAAAAAAAAAAAAAAAAAAAA")

    @discord.ui.button(style=discord.ButtonStyle.red, label="Task canceled !")
    async def taskFailed(interaction: discord.Interaction, Button: discord.ui.Button):
        print("BBBBBBBBBBBBBBBBBBBBBBBBBB")