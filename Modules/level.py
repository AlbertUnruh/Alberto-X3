from discord import Embed, Client, Message, Role
from Utils import Help, EVENT, send_exception, DATA, Prefix

from sqlite3 import connect
from random import choice
from typing import Tuple, Dict
from datetime import datetime, timedelta


HELP = Help("shows you your XP", f"{Prefix}level (iD/ping)", order_1793=True)
EVENTS = [EVENT.on_message]
ALIASES = ["lvl", "rank"]

possible_xps = [3, 3,
                4, 4, 4, 4,
                5, 5, 5,
                6, 6,
                7]
free = "<:XP0:831578582026813480>"
full = "<:XP1:831578621092691978>"
len_bar = 20
formula = 1/4.5
latency = timedelta(minutes=1)

lvl_rewards = {
    "25": 831628612171071498,
    "20": 831628364803997757,
    "15": 831628201406627871,
    "10": 831628459222237227
}
recent: Dict[int, datetime] = {}


async def __main__(client: Client, _event: int, message: Message):
    try:
        if any((message.author.bot,
                message.guild is None)):
            return

        try:
            user = int(message.content.split()[-1].replace("<", "")
                                                  .replace("@", "")
                                                  .replace("!", "")
                                                  .replace(">", ""))
            message.author = message.guild.get_member(user) or message.author
        except TypeError:
            user = message.author.id

        db = connect("levels.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM lvl WHERE user=={user}")

        fetched = cursor.fetchone()
        if fetched is None:
            cursor.execute(f"INSERT INTO lvl VALUES ({user}, 0, 0)")
            db.commit()

        data: Tuple[int, int, int] = fetched or (user, 0, 0)

        xp = data[2]
        lvl = data[1]

        if message.content.startswith(Prefix):
            user_level = xp ** formula
            user_progress = int(str(user_level).split(".")[1][:2])
            len_filled = int(len_bar*user_progress/100)

            bar = f"{'#' * len_filled:-<{len_bar}}"
            bar = bar.replace("#", full)
            bar = bar.replace("-", free)

            cursor.execute(f"SELECT level FROM lvl where xp>{xp}")
            rank = len(cursor.fetchall()) + 1

            embed = Embed(color=0x275591,
                          description=f"You are the number __**#{rank}**__!")
            embed.set_author(name=message.author.name,
                             icon_url=message.author.avatar_url)

            embed.add_field(inline=False,
                            name="Your LVL:", value=str(lvl))
            embed.add_field(inline=False,
                            name="Your XP:", value=f"{xp}\n{bar}")

            await message.channel.send(embed=embed)
            return

        # below is only without prefix and just leveling

        try:
            if recent[user]+latency > datetime.utcnow():
                return
        except KeyError:
            pass

        recent[user] = datetime.utcnow()

        xp += choice(possible_xps)
        old_lvl = lvl
        lvl = int(xp ** formula) - 1

        cursor.execute(f"UPDATE lvl SET level={lvl} WHERE user=={user}")
        cursor.execute(f"UPDATE lvl SET xp={xp} WHERE user=={user}")

        db.commit()
        db.close()

        if lvl != old_lvl:
            await client.get_channel(831625194803298314).send(
                f"Congratulations __**{message.author.mention}**__!\n"
                f"You are now __*Level {lvl}*__ 🥳🥳🥳\n")

            if str(lvl) in lvl_rewards:
                reward: Role = message.guild.get_role(lvl_rewards[str(lvl)])
                await message.author.add_role(reward, "Leveling reward")

    except Exception as e:
        await send_exception(client=client, exception=e, source_name=__name__)
