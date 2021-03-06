import discord

from typing import *
from NewClass import AttrDict
from json import load

from traceback import format_exc
from io import BytesIO


'''
You can see all the events in the following URL:
https://discordpy.readthedocs.io/en/latest/api.html#event-reference
'''


EVENT = AttrDict({
    "on_connect":                       0,  # argument(s) --> client: discord.Client, _event: int
    "on_shard_connect":                 1,  # argument(s) --> client: discord.Client, _event: int, shard_id: int
    "on_disconnect":                    2,  # argument(s) --> client: discord.Client, _event: int
    "on_shard_disconnect":              3,  # argument(s) --> client: discord.Client, _event: int, shard_id: int
    "on_ready":                         4,  # argument(s) --> client: discord.Client, _event: int
    "on_shard_ready":                   5,  # argument(s) --> client: discord.Client, _event: int, shard_id: int
    "on_resumed":                       6,  # argument(s) --> client: discord.Client, _event: int
    "on_shard_resumed":                 7,  # argument(s) --> client: discord.Client, _event: int, shard_id: int
    "on_error":                         8,  # argument(s) --> client: discord.Client, _event: int, event: str, *args, **kwargs
    "on_socket_raw_receive":            9,  # argument(s) --> client: discord.Client, _event: int, message: Union[bytes, str]
    "on_socket_raw_send":              11,  # argument(s) --> client: discord.Client, _event: int, payload: Union[bytes, str]
    "on_typing":                       12,  # argument(s) --> client: discord.Client, _event: int, channel: discord.abc.Messageable, user: Union[discord.User, discord.Member], when: datetime.datetime
    "on_message":                      13,  # argument(s) --> client: discord.Client, _event: int, message: discord.Message
    "on_message_delete":               14,  # argument(s) --> client: discord.Client, _event: int, message: discord.Message
    "on_bulk_message_delete":          15,  # argument(s) --> client: discord.Client, _event: int, messages: List[discord.Message]
    "on_raw_message_delete":           16,  # argument(s) --> client: discord.Client, _event: int, payload: discord.RawMessageDeleteEvent
    "on_message_edit":                 17,  # argument(s) --> client: discord.Client, _event: int, before: discord.Message, after: discord.Message
    "on_raw_message_edit":             18,  # argument(s) --> client: discord.Client, _event: int, payload: discord.RawMessageUpdateEvent
    "on_reaction_add":                 19,  # argument(s) --> client: discord.Client, _event: int, reaction: discord.Reaction, user: Union[discord.Member, discord.User]
    "on_raw_reaction_add":             20,  # argument(s) --> client: discord.Client, _event: int, payload: discord.RawReactionActionEvent
    "on_reaction_remove":              21,  # argument(s) --> client: discord.Client, _event: int, reaction: discord.Reaction, user: Union[discord.Member, discord.User]
    "on_raw_reaction_remove":          22,  # argument(s) --> client: discord.Client, _event: int, payload: discord.RawReactionActionEvent
    "on_reaction_clear":               23,  # argument(s) --> client: discord.Client, _event: int, message: discord.Message, reactions: List[discord.Reaction]
    "on_raw_reaction_clear":           24,  # argument(s) --> client: discord.Client, _event: int, payload: discord.RawReactionClearEvent
    "on_reaction_clear_emoji":         25,  # argument(s) --> client: discord.Client, _event: int, reaction: discord.Reaction
    "on_raw_reaction_clear_emoji":     26,  # argument(s) --> client: discord.Client, _event: int, payload: discord.RawReactionClearEmojiEvent
    "on_private_channel_delete":       27,  # argument(s) --> client: discord.Client, _event: int, channel: discord.abc.PrivateChannel
    "on_private_channel_create":       28,  # argument(s) --> client: discord.Client, _event: int, channel: discord.abc.PrivateChannel
    "on_private_channel_update":       29,  # argument(s) --> client: discord.Client, _event: int, before: discord.GroupChannel, after: discord.GroupChannel
    "on_private_channel_pins_update":  30,  # argument(s) --> client: discord.Client, _event: int, channel: discord.abc.PrivateChannel, last_pin: Optional[datetime.datetime]
    "on_guild_channel_delete":         31,  # argument(s) --> client: discord.Client, _event: int, channel: discord.abc.GuildChannel
    "on_guild_channel_create":         32,  # argument(s) --> client: discord.Client, _event: int, channel: discord.abc.GuildChannel
    "on_guild_channel_update":         33,  # argument(s) --> client: discord.Client, _event: int, before: discord.GroupChannel, after: discord.GroupChannel
    "on_guild_channel_pins_update":    34,  # argument(s) --> client: discord.Client, _event: int, channel: discord.abc.PrivateChannel, last_pin: Optional[datetime.datetime]
    "on_guild_integrations_update":    35,  # argument(s) --> client: discord.Client, _event: int, guild: discord.Guild
    "on_webhooks_update":              36,  # argument(s) --> client: discord.Client, _event: int, channel: discord.abc.GuildChannel
    "on_member_join":                  37,  # argument(s) --> client: discord.Client, _event: int, member: discord.Member
    "on_member_remove":                38,  # argument(s) --> client: discord.Client, _event: int, member: discord.Member
    "on_member_update":                39,  # argument(s) --> client: discord.Client, _event: int, before: discord.Member, after: discord.Member
    "on_user_update":                  40,  # argument(s) --> client: discord.Client, _event: int, before: discord.User, after: discord.User
    "on_guild_join":                   41,  # argument(s) --> client: discord.Client, _event: int, guild: discord.Guild
    "on_guild_remove":                 42,  # argument(s) --> client: discord.Client, _event: int, guild: discord.Guild
    "on_guild_update":                 43,  # argument(s) --> client: discord.Client, _event: int, before: discord.Guild, after: discord.Guild
    "on_guild_role_create":            44,  # argument(s) --> client: discord.Client, _event: int, role: discord.Role
    "on_guild_role_delete":            45,  # argument(s) --> client: discord.Client, _event: int, role: discord.Role
    "on_guild_role_update":            46,  # argument(s) --> client: discord.Client, _event: int, before: discord.Role, after: discord.Role
    "on_guild_emojis_update":          47,  # argument(s) --> client: discord.Client, _event: int, guild: discord.Guild, before: Sequence[discord.Emoji], after: Sequence[discord.Emoji]
    "on_guild_available":              48,  # argument(s) --> client: discord.Client, _event: int, guild: discord.Guild
    "on_guild_unavailable":            49,  # argument(s) --> client: discord.Client, _event: int, guild: discord.Guild
    "on_voice_state_update":           50,  # argument(s) --> client: discord.Client, _event: int, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState
    "on_member_ban":                   51,  # argument(s) --> client: discord.Client, _event: int, guild: discord.Guild, user: Union[discord.User, discord.Member]
    "on_member_unban":                 52,  # argument(s) --> client: discord.Client, _event: int, guild: discord.Guild, user: discord.User
    "on_invite_create":                53,  # argument(s) --> client: discord.Client, _event: int, invite: discord.Invite
    "on_invite_delete":                54,  # argument(s) --> client: discord.Client, _event: int, invite: discord.Invite
    "on_group_join":                   55,  # argument(s) --> client: discord.Client, _event: int, channel: discord.GroupChannel, user: discord.User
    "on_group_remove":                 56,  # argument(s) --> client: discord.Client, _event: int, channel: discord.GroupChannel, user: discord.User
})


DATA = AttrDict(load(open("Configs.json")))
Prefix = DATA.CONSTANTS.Prefix


class Help(object):
    direct_help_default = "*Please contact the developer to add a help for this!*"

    def __init__(self, _help: Optional[str] = None, direct_help: Union[str, bool] = False,
                 vanish: bool = False, order_1793: bool = False, order_2004: bool = False):
        """
        _help: :class:`str`
            is the printed value of the help
        direct_help: :class:Union[`str`,`bool`]
            is the printed value of the help when this function is called, when it is a `str`,
            if it's `True` it is the `direct_help_default`, otherwise it's `_help`
        vanish: :class:`bool`
            makes it invisible
        order_1793: :class:`bool`
            activates it every time when a message without the prefix was send
        order_2004: :class:`bool`
            activates it every time when a message was send
        """

        self.help = _help
        if isinstance(direct_help, str):
            self.direct_help = direct_help
        elif direct_help:
            self.direct_help = self.direct_help_default
        else:
            self.direct_help = self.help
        self.vanish = vanish
        self.order_1793 = order_1793
        self.order_2004 = order_2004

        if self.order_1793 is True and self.order_2004 is True:
            self.order_1793 = False

    def __str__(self):
        return self.help if self.supports() else "There is no help set!"

    def supports(self):
        return False if self.help is None else True


class Logger:
    from datetime import datetime

    def __init__(self, channel: discord.TextChannel) -> None:
        self.channel = channel
        self.messages = AttrDict({
            "join":            "*{}* joined this server! ID: {}; account creation: {}, {} days ago",
            "left":            "*{}* left this server! ID: {}; account creation: {}, {} days ago; server joined: {}, {} days ago",
            "rules":           "*{}* accepted the rules",
            "kick":            "*{}* kicked *{}* with reason *{}*",
            "ban":             "*{}* banned *{}* with reason *{}*",
            "unban":           "*{}* unbanned *{}* with reason *{}*",
            "softban":         "*{}* softbanned *{}* with reason *{}*",
            "delete":          "*{}* deleted *{}* messages in *{}*",
            "not implemented": "{}; {}; {}; {}; {}"
        })

    async def join(self,
                   member: discord.Member
                   ) -> None:
        await self.channel.send(
            self.messages.join.format(member.mention, member.id, member.created_at, (self.datetime.now() - member.created_at).days)
        )

    async def left(self,
                   member: discord.Member
                   ) -> None:
        await self.channel.send(
            self.messages.left.format(member.mention, member.id, member.created_at, (self.datetime.now() - member.created_at).days, member.joined_at, (self.datetime.now() - member.joined_at).days)
        )

    async def rules(self,
                    user: discord.User
                    ) -> None:
        await self.channel.send(
            self.messages.rules.format(user.mention)
        )

    async def kick(self,
                   user: discord.User,
                   target: discord.User,
                   reason: str
                   ) -> None:
        await self.channel.send(
            self.messages.kick.format(user.mention, target.mention, reason)
        )

    async def ban(self,
                  user: discord.User,
                  target: discord.User,
                  reason: str
                  ) -> None:
        await self.channel.send(
            self.messages.ban.format(user.mention, target.mention, reason)
        )

    async def unban(self,
                    user: discord.User,
                    target: discord.User,
                    reason: str
                    ) -> None:
        await self.channel.send(
            self.messages.unban.format(user.mention, target.mention, reason)
        )

    async def softban(self,
                      user: discord.User,
                      target: discord.User,
                      reason: str
                      ) -> None:
        await self.channel.send(
            self.messages.softban.format(user.mention, target.mention, reason)
        )

    async def delete(self,
                     user: discord.User,
                     count: int,
                     channel: discord.TextChannel
                     ) -> None:
        await self.channel.send(
            self.messages.delete.format(user.mention, count, channel.mention)
        )

    async def not_implemented(self,
                              content: str = None,
                              user: discord.User = None,
                              target: discord.User = None,
                              comments: str = None,
                              channel: discord.TextChannel = None
                              ) -> None:
        await self.channel.send(
            self.messages.not_implemented.format(f"{content=}", f"{user=}", f"{target=}", f"{comments=}", f"{channel=}")
        )


def perms(_id: str) -> AttrDict:
    from json import load, dump

    PERMS = AttrDict(load(open("perms.json")))
    try:
        user_perms = PERMS[_id]
    except KeyError:
        user_perms = PERMS.default
        PERMS[_id] = user_perms
        dump(PERMS, open("perms.json", "w"), indent=2)

    return user_perms


async def send_exception(client: discord.Client, exception: Exception, source_name: str, mention_role: Optional[int] = 820974562770550816, pin: bool = True, timestamp: bool = True):
    """
    sends the exception into a channel if `DATA.debug` ist disabled
    """
    if not DATA.debug:
        super_log: discord.TextChannel = client.get_channel(DATA.IDs.Channels.Super_Log)

        file = discord.File(BytesIO(format_exc().encode()), "exception.log")
        embed: discord.Embed = discord.Embed(title=source_name,
                                             description=f"{exception.__class__.__name__}: {exception.__str__()}\n",
                                             color=discord.Color.magenta())

        message: discord.Message = await super_log.send(embed=embed, file=file)

        if timestamp:
            from discord.utils import snowflake_time
            embed.add_field(name="datetime.datetime",
                            value=snowflake_time(message.id).__str__())
            await message.edit(embed=embed)
        if pin:
            await message.pin()
        if mention_role:
            await super_log.send(f"<@&{mention_role}>")
    else:
        raise exception
