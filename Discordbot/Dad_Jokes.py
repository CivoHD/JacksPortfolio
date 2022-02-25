
import discord
import nextcord
import random
import anime_images_api
import dadjokes
from nextcord.ext import commands

dadjoke = dadjokes


class dadCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dj(self, ctx):
        await ctx.send(dadjoke.joke())
