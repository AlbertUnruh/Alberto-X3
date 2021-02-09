import discord
import Utils


HELP = Utils.Help("shows the ping")
EVENTS = [Utils.EVENT.on_message]
ALIASES = [":ping_pong:"]


async def __main__(client: discord.Client, _event: int, message: discord.Message):
    await message.channel.send(f"Pong :ping_pong:\nI have a latency from {round(client.latency, 2)} seconds")
