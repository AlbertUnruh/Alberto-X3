import discord
import Utils


HELP = Utils.Help(f"bans and unbans a user to delete all messages from the user", f"_{Utils.Prefix}hardkick iD (reason)_\requires Admin.softban")
EVENTS = [Utils.EVENT.on_message]
ALIASES = ["hk"]


async def __main__(client: discord.Client, _event: int, message: discord.Message):
    try:
        user_perms = Utils.perms(str(message.author.id))

        if user_perms.Admin.softban:
            if len(message.content.split()) >= 2:
                if message.content.split()[1].isnumeric():
                    if len(message.content.split()) > 2:
                        reason = " ".join(message.content.split()[2:])
                    else:
                        reason = "No reason..."

                    logger = Utils.Logger(channel=await client.fetch_channel(Utils.DATA.IDs.Channels.Logs))
                    channel: discord.TextChannel = message.channel
                    guild:         discord.Guild = message.guild
                    user:           discord.User = await client.fetch_user(int(message.content.split()[1]))
                    handler:        discord.User = message.author

                    try:
                        await user.send(f"You where hardkicked from the {guild} Server.\n**Please be friendly, otherwise we can make it to a permanent one!!!**\n_{reason}_")
                        await guild.ban(user=user, reason="SOFTBAN | "+reason)
                        await guild.unban(user=user, reason="SOFTBAN | "+reason)
                        await logger.softban(user=handler, target=user, reason=reason)
                        await message.delete()
                    except ValueError:
                        await channel.send(":x: ERROR :x:")
                    except discord.Forbidden:
                        pass

                else:
                    await message.channel.send(":x: Please enter the User-iD")
            else:
                await message.channel.send(":x: Please enter the User-iD")

        else:
            await message.channel.send(":x: requires Admin.softban")

    except Exception as e:
        await Utils.send_exception(client=client, exception=e, source_name=__name__)
