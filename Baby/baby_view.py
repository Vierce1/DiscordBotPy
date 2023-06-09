import helpers
from discord.ext import commands
import discord
from discord import app_commands
import discord.ext
from Baby.baby import BabyStuff
import asyncio

class BabyView(discord.ui.View):
    def __init__(self, baby: BabyStuff, baby_name: str, rater: str, orig_message: discord.Interaction,
                 backfilling: bool):
        super().__init__()
        # super().__init__(timeout=5)
        self.score = None
        self.baby = baby
        self.baby_name = baby_name
        self.rater = rater
        self.orig_message = orig_message
        self.callback = self.baby.submit_name_score if not backfilling \
            else self.baby.submit_previous_name_score

    async def on_timouet(self):
        print("timeout")
        self.clear_items()
        self.refresh()


    @discord.ui.button(label="1", style=discord.ButtonStyle.red)
    async def one(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 1
        print("scored 1")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()

    @discord.ui.button(label="2", style=discord.ButtonStyle.red)
    async def two(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 2
        print("scored 2")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()

    @discord.ui.button(label="3", style=discord.ButtonStyle.red)
    async def three(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 3
        print("scored 3")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()

    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)
    async def four(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 4
        print("scored 4")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()

    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)
    async def five(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 5
        print("scored 5")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()

    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)
    async def six(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 6
        print("scored 6")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()

    @discord.ui.button(label="7", style=discord.ButtonStyle.green)
    async def seven(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 7
        print("scored 7")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()

    @discord.ui.button(label="8", style=discord.ButtonStyle.green)
    async def eight(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 8
        print("scored 8")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()

    @discord.ui.button(label="9", style=discord.ButtonStyle.green)
    async def nine(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 9
        print("scored 9")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()

    @discord.ui.button(label="10", style=discord.ButtonStyle.green)
    async def ten(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = helpers.get_user_name(interaction)
        if helpers.get_name(user) != self.rater:
            await self.orig_message.followup.send("Please use your own rating box.")
            return
        self.score = 10
        print("scored 10")
        button.callback = await self.callback(self.score, self.baby_name, interaction, self.rater)
        self.stop()