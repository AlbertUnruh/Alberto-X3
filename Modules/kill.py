import discord
import Utils

from json import load


HELP = Utils.Help("requires Admin.Bot.kill\n~~kills the Bot...~~ really dangerous")
EVENTS = [Utils.EVENT.on_message]


async def __main__(client: discord.Client, _event: int, message: discord.Message):

    user_perms = Utils.perms(str(message.author.id))

    if user_perms.Admin.Bot.kill:
        author = await client.fetch_user(Utils.AttrDict(load(open("./Configs.json"))).Author_id)
        await author.send(f"**__starting kill by {message.author}__**")
        await client.close()

        input("Press <ENTER>...")

    else:
        await message.channel.send(":x: requires Admin.Bot.kill")
