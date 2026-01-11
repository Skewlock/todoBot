import discord, os

botIntents = discord.Intents.all()

bot = discord.Client(intents=botIntents)
bot.prefix = "!"

@bot.event
async def on_message(msg):
    # Get command
    if msg.author == bot.user:
        return

    if msg.content[0] != bot.prefix:
        return

    instruction = msg.content[1:]
    command = instruction.split(" ")[0]
    logs.printInfo("Command " + command + " requested.")

    commands = {
        #General commands
        "ping": [cmds.ping, (msg, bot)]
    }

    # Launch command
    func = commands.get(command)
    if func is None:
        return logs.printWarning("Command " + command + " doesn't exists.\n")
    await func[0](*func[1])
    logs.printInfo("Command " + command + " successfully done.\n")


@bot.event
async def on_ready():
    logs.printValid("Bot ready !")
    logs.printValid("Default prefix: " + bot.prefix)
    logs.printValid("Mention: " + bot.user.mention + "\n")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("prefix: "+ bot.prefix))

bot.run(os.environ["TOKEN"])