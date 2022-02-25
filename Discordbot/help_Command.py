
import nextcord
from nextcord.ext import commands


class helpCommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = nextcord.Embed(
            title='Help', description="Shows all commands that are useable", color=nextcord.Colour.random())

        em.add_field(name="Action Gifs", value="!punch, !kick")
        em.add_field(name="Dad Jokes", value="!dj")
        em.add_field(name="Fun Commands",
                     value="!coolrate, !epicgamerrate, !eightball")
        em.add_field(name="Google Image", value="!showpic <image name>")
        em.add_field(name="Truth or Dare", value="!truth, !dare")
        em.add_field(name="About", value="!about")

        await ctx.send(embed=em)

    @commands.group(invoke_without_command=True)
    async def about(self, ctx):
        em = nextcord.Embed(
            title='About', color=nextcord.Colour.random())

        em.add_field(
            name="About the Bot", value="This bot is too display a project that i did for my portfolio")

        await ctx.send(embed=em)

    