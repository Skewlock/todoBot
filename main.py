import discord, os, time
from discord.ext import commands
from discord import app_commands
from users import User
import ui
import logs

GUILD_ID = discord.Object(id=1459887017470201939)
CATEGORY_ID = 1459947666653057096

miel = User(channel_id=1459948940202872913, user_id=250711124557824001)
kawa = User(channel_id=1459948924679880909, user_id=962368208705323069)

users = [miel, kawa]

class Client(commands.Bot):

    async def on_ready(self):
        logs.printValid("Bot ready !")
        logs.printValid("Default prefix: " + self.command_prefix)
        logs.printValid("Mention: " + self.user.mention + "\n")
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("C le baute isi"))
        try:
            synced = await self.tree.sync(guild=GUILD_ID)
            print(f'Synced {len(synced)} commands to guild {GUILD_ID.id}')
        except Exception as e:
            print("Error syncing command: " + str(e))


    async def on_message(self, msg):
        # Get command
        if msg.author == self.user:
            return

        if msg.content[0] != self.command_prefix:
            return
        return


botIntents = discord.Intents.all()
bot = Client(command_prefix="!", intents=botIntents)

@bot.tree.command(
    name="ping",
    description="[DEBUG COMMAND] pong",
    guild=GUILD_ID
)
async def ping(interaction: discord.Interaction):
    time_then = time.monotonic()
    pinger = await interaction.response.send_message("Pinging...")
    ping_ = (1000 * (time.monotonic() - time_then))
    embed = discord.Embed(title="Results :", color=0x4c99c2, type="rich")
    embed.add_field(name="Bot ping :", value=str(int(ping_)) + "ms", inline=True)
    embed.add_field(name="API ping :", value=str(int(bot.latency * 1000)) + "ms", inline=True)
    await pinger.resource.edit(content=":white_check_mark: Done !", embed=embed)

@bot.tree.command(
    name="create_task",
    description="Create a task on someone's todolist",
    guild=GUILD_ID
)
async def create_task(interaction: discord.Interaction, task_name: str, task_owner: discord.Member):
    channel = None
    for i in users:
        if i.user_id == task_owner.id:
            channel = i.channel_id
    if channel == None:
        interaction.response.send_message("Task owner isn't registered in the system, please inform Miel if this needs to be fixed.")
    else:
        chan = interaction.guild.get_channel(channel)
        created = int(time.time())
        embed = discord.Embed(title=task_name, color=0xfcba03, type='rich')
        embed.add_field(name="Created:", value=f"<t:{created}:R>")
        await chan.send("Nouvelle Tâche pour " + task_owner.mention + ": " + task_name, view=ui.TaskView(), embed=embed)
        await interaction.response.send_message("Task created in " + chan.mention)


bot.run(os.environ["TOKEN"])