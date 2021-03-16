import discord
import Utils


HELP = Utils.Help(vanish=True, order_1793=True)
EVENTS = [Utils.EVENT.on_message]


async def __main__(client: discord.Client, _event: int, message: discord.Message):
    try:
        if message.content == client.user.mention:
            await message.channel.send(f"My Prefix is `{Utils.Prefix}`")

    except Exception as e:
        from discord.utils import snowflake_time

        super_log: discord.TextChannel = client.get_channel(Utils.DATA.IDs.Channels.Super_Log)
        embed: discord.Embed = discord.Embed(title=__name__,
                                             description=f"{e.__class__.__name__}: {e.__str__()}\n",
                                             color=discord.Color.magenta())

        message: discord.Message = await super_log.send(embed=embed)

        embed.add_field(name="datetime.datetime",
                        value=snowflake_time(message.id).__str__())
        await message.edit(embed=embed)
        await message.pin()
        await super_log.send(f"<@&{820974562770550816}>", delete_after=0)
