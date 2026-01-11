import discord, os, time
from discord.ext import commands
from discord import app_commands
import logs

GUILD_ID = discord.Object(id=1459887017470201939)

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

        if msg.content[0] != self.prefix:
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
    pinger = await interaction.response.send_message("Calcul en cours du ping...")
    ping_ = (1000 * (time.monotonic() - time_then))
    embed = discord.Embed(title="Results :", color=0x4c99c2, type="rich")
    embed.add_field(name="Ping du bot :", value=str(int(ping_)) + "ms", inline=True)
    embed.add_field(name="Ping de l'API :", value=str(int(bot.latency * 1000)) + "ms", inline=True)
    await pinger.edit_message(content=":white_check_mark: Calcul terminé !", embed=embed)

@bot.tree.command(
    name="create_task",
    description="Crée une tâche dans la todo list",
    guild=GUILD_ID
)
async def create_task(interaction: discord.Interaction, task_name: str):
    await interaction.response.send_message("test")


bot.run(os.environ["TOKEN"])