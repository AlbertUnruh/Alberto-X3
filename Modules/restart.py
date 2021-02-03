import discord
import Utils

from json import load


HELP = Utils.Help("requires Admin.Bot.restart")
EVENTS = [Utils.EVENT.on_message]


async def __main__(client: discord.Client, _event: int, message: discord.Message):

    user_perms = Utils.perms(str(message.author.id))

    if user_perms.Admin.Bot.restart:
        author = await client.fetch_user(Utils.AttrDict(load(open("./Configs.json"))).Author_id)
        await author.send(f"**__starting restart by {message.author}__**")
        await client.change_presence(status=discord.Status.offline)
        await client.close()

    else:
        await message.channel.send(":x: requires Admin.Bot.restart")
