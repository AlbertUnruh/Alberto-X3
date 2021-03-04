import discord
import Utils


HELP = Utils.Help(vanish=True, order_1793=True)
EVENTS = [Utils.EVENT.on_message]


async def __main__(client: discord.Client, _event: int, message: discord.Message):
    try:
        if message.content == client.user.mention:
            await message.channel.send(f"My Prefix is `{Utils.Prefix}`")

    except Exception as e:
        super_log: discord.TextChannel = client.get_channel(Utils.DATA.IDs.Channels.Super_Log)

        embed: discord.Embed = discord.Embed(title=__name__, description=e)

        await super_log.send(embed=embed)
