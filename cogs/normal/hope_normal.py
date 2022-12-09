""""
Copyright © Krypton 2022 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
This is a template to create your own discord bot in python.

Version: 4.1.1
"""

from datetime import datetime
from typing import Callable
import json
import os
import sys
import csv

from disnake import File, Role
from disnake.ext import commands
from disnake.ext.commands import Context
import pytz

from helpers import cache, checks

assets_prefix = "assets/"

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class Hope(commands.Cog, name="spacing"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="prune",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def prune(self, context: Context) -> None:
        if len(context.message.content.split(" ")) < 1:
            return

        value = context.message.content.split(" ")[1]
        await context.channel.purge(limit=int(value), check=lambda msg: not msg.pinned )
        # await context.send(f"{value} messages deleted.")

    @commands.command(
        name="autoprune",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def auto_prune(self, context: Context) -> None:
        if len(context.message.content.split(" ")) < 1:
            return

        value = context.message.content.split(" ")[1]

        if value == "pop":
            currents = set(cache.prune_channel)
            pops = set(list(map(lambda x: x.id, context.message.channel_mentions)))
            cache.prune_channel = list(currents.difference(pops))
            await context.send("Remove channels from prune list.")

        if value == "push":
            cache.prune_channel += list(
                map(lambda x: x.id, context.message.channel_mentions)
            )
            channels = list(set(cache.prune_channel))
            await context.send(f"Add channels to prune list.")
            for id in channels:
                await context.send(self.bot.get_channel(id).mention)

        if value == "clear":
            cache.prune_channel = []
            await context.send("Wipe auto prune log.")

        if value == "list":
            for id in cache.prune_channel:
                await context.send(self.bot.get_channel(id).mention)

    @commands.command(
        name="waifu",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def waifu_command(self, context: Context) -> None:
        """
        This is a command that send an image.
        :param context: The context in which the command has been executed.
        """
        # await context.channel.send("Kiana is the best waifu.")
        # skip first character which is the prefix
        content = context.message.content[1:]
        file = open("helpers/name_binding.json", "r")
        name_binding = json.load(file)
        text = name_binding[content] if content in name_binding else content
        await context.send(file=File(assets_prefix + text + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="inrole",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def inrole_command(self, context: Context) -> None:
        """
        blabla
        :param context: The context in which the command has been executed.
        """
        content = context.message.content[1:]
        lst = content.split(" ")
        members = []
        to_list: Callable[[Role], list] = lambda role : [[f'{member.name}#{member.discriminator}', f"'{member.id}"] for member in role.members]
        appendMember: Callable[[list], None] = lambda lst : [members.append(member) for member in lst if not member in members]
        if content == 'inrole':
            await context.channel.send("Hello world!")
            return
        if 'lh' in lst:
            role = context.guild.get_role(387517990427426816)
            if not role is None: appendMember(to_list(role))
        if 'eh' in lst:
            role = context.guild.get_role(503537635508355083)
            if not role is None: 
                for member in to_list(role) : members.append(member)
        if 'ah' in lst:
            role = context.guild.get_role(819625842681315328)
            if not role is None: 
                for member in to_list(role) : members.append(member)
        if 'hh' in lst:
            role = context.guild.get_role(478857442562801666)
            if not role is None: 
                for member in to_list(role) : members.append(member)
        if 'wh' in lst:
            role = context.guild.get_role(585144949520072720)
            if not role is None: 
                for member in to_list(role) : members.append(member)
        if 'guest' in lst:
            role = context.guild.get_role(729922674289147935)
            if not role is None: 
                for member in to_list(role) : members.append(member)
        if 'kibous' in lst:
            role = context.guild.get_role(405675971824320513)
            if not role is None: 
                for member in to_list(role) : members.append(member)
        if 'slave' in lst:
            role = context.guild.get_role(745289897245671476)
            if not role is None: appendMember(to_list(role))
        if members == []: 
            await context.channel.send("No role found.")
        else:
            header = ['Member', 'ID']
            filename='members.csv'
            file = open(filename, "w", encoding='utf-16', newline='')
            writer = csv.writer(file, delimiter='\t' )
            writer.writerow(header)
            writer.writerows(members)
            file.close()
            await context.channel.send(file=File(filename))
    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="join",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def join_command(self, context: Context) -> None:
        """
        This is a command that send an image.
        :param context: The context in which the command has been executed.
        """
        # await context.channel.send("Kiana is the best waifu.")
        content = context.message.content[1:]
        file = open("helpers/name_binding.json", "r")
        name_binding = json.load(file)
        text = name_binding[content] if content in name_binding else content
        await context.send(file=File(assets_prefix + text + ".gif"))
        await context.channel.send("Hello world!")

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="interactive",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def interactive_command(self, context: Context) -> None:
        """
        blabla
        """
        await context.channel.send(file=File(assets_prefix + "wink.jpg"))
        await context.channel.send("Some interactive text")

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="general",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def general_command(self, context: Context) -> None:
        await context.channel.send(file=File(assets_prefix + "wink.jpg"))
        await context.channel.send("Some general text")

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="picture",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def picture_command(self, context: Context) -> None:
        await context.channel.send("Some picture text")

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="gif",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def gif_command(self, context: Context) -> None:
        await context.channel.send("Some gif text")

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="armada",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def armada_command(self, context: Context) -> None:
        content = context.message.content[1:]
        command = content.split(" ")[1]
        if command == "list":
            await context.channel.send(file=File(assets_prefix + "armada list.png"))
            await context.channel.send("Some armada list text")
        else:
            await context.channel.send("Some armada text")

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="allhope",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def allhope_command(self, context: Context) -> None:
        content = context.message.content[1:]
        message = " ".join(content.split(" ")[1:])
        await context.send(message)
        await context.send("some all hope text")

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="allcore",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def allcore_command(self, context: Context) -> None:
        content = context.message.content[1:]
        message = " ".join(content.split(" ")[1:])
        await context.send(message)
        await context.send("some all core text")

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="reload",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def reload_command(self, context: Context) -> None:
        if len(cache.prune_cache) > 0:
            text = cache.prune_cache[-1].content
            await context.send(text)
            await context.send("some reload text")

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="intro",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def intro_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "intro" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="screenshot",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def screenshot_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "screenshot" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="rules",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def rules_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "rules" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="yes",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def yes_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p yes" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="no",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def no_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p no" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="lol",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def lol_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p lol" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="ara",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def ara_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p ara" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="argh",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def argh_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p arght" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="cute",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def cute_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p cute" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="hehe",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def hehe_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p hehe" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="lmao",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def lmao_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p lmao" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="bonk",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def bonk_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p bonk" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="teehee",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def teehee_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p teehee" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="updating",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def updating_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p updating" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="stupidest",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def stupidest_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p stupidest" + ".jpg"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="QTE",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def qte_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p qte" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="tuna",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def tuna_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p tuna" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="salt",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def salt_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p salt" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="haha",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def haha_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p haha" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="kiss",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def kiss_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p kiss" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="judah",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def judah_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p judah" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="combo",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def combo_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p combo" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="affix",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def affix_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p affix" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="whale",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def whale_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p whale" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="oraora",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def oraora_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p oraora" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="mudamuda",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def mudamuda_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p mudamuda" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="shuppatsu",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def shuppatsu_command(self, context: Context) -> None:
        await context.send(file=File(assets_prefix + "p shuppatsu" + ".gif"))

    # ----------------------------------------------------------------------------------------------

    @commands.command(
        name="time",
        description="This one gonna be awesome.",
    )
    @checks.not_blacklisted()
    async def time_command(self, context: Context) -> None:
        tz = pytz.timezone('Asia/Singapore')
        await context.send(f"{datetime.now(tz).strftime('%H:%M:%S')}")
# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.


def setup(bot):
    bot.add_cog(Hope(bot))
