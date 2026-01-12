import discord

class TaskView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(style=discord.ButtonStyle.green, label="Finish task", custom_id="todo:check")
    async def taskDone(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed_title = interaction.message.embeds[0].title
        created = interaction.message.embeds[0].fields[0].value
        desc = interaction.message.embeds[0].description
        mention = interaction.message.mentions[0].mention
        msg_content = "New task for " + mention + ": " + embed_title

        embed = discord.Embed(title=embed_title, color=discord.Colour.green(), description=desc, type='rich')
        embed.add_field(name="Created:", value=created)
        embed.add_field(name="Status:", value=":white_check_mark: Success")
        await interaction.message.edit(content=msg_content, view=TaskView(), embed=embed)
        await interaction.response.send_message('Task marked as success !', ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="Repoen task", custom_id="todo:reopened")
    async def taskReopened(self, interaction: discord.Interaction, Button: discord.ui.Button):
        embed_title = interaction.message.embeds[0].title
        created = interaction.message.embeds[0].fields[0].value
        desc = interaction.message.embeds[0].description
        mention = interaction.message.mentions[0].mention
        msg_content = "New task for " + mention + ": " + embed_title

        embed = discord.Embed(title=embed_title, color=discord.Colour.blurple(), description=desc, type='rich')
        embed.add_field(name="Created:", value=created)
        embed.add_field(name="Status:", value=":up: Open")
        await interaction.message.edit(content=msg_content, view=TaskView(), embed=embed)
        await interaction.response.send_message('Task reopened', ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.red, label="Cancel task", custom_id="todo:failed")
    async def taskFailed(self, interaction: discord.Interaction, Button: discord.ui.Button):
        embed_title = interaction.message.embeds[0].title
        created = interaction.message.embeds[0].fields[0].value
        desc = interaction.message.embeds[0].description
        mention = interaction.message.mentions[0].mention
        msg_content = "New task for " + mention + ": " + embed_title

        embed = discord.Embed(title=embed_title, color=discord.Colour.red(), description=desc, type='rich')
        embed.add_field(name="Created:", value=created)
        embed.add_field(name="Status:", value=":no_entry: Cancelled")
        await interaction.message.edit(content=msg_content, view=TaskView(), embed=embed)
        await interaction.response.send_message('Task marked as failed', ephemeral=True)