import discord, time

async def ping(msg, bot):
    time_then = time.monotonic()
    pinger = await msg.channel.send("Calcul en cours du ping...")
    ping_ = (1000 * (time.monotonic() - time_then))
    embed = discord.Embed(title="Results :", color=0x4c99c2, type="rich")
    embed.add_field(name="Ping du bot :", value=str(int(ping_)) + "ms", inline=True)
    embed.add_field(name="Ping de l'API :", value=str(int(bot.latency * 1000)) + "ms", inline=True)
    await pinger.edit(content=":white_check_mark: Calcul terminé !", embed=embed)


async def create_task(interaction):
    await interaction.response.send_message("test")