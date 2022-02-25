
import nextcord
import random
from nextcord.ext import commands


class funCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong")

    # RATE COMMANDS
    @commands.command()
    async def coolrate(self, ctx):
        embed = nextcord.Embed(
            title="cool rate machine",
            description=f"You're are {random.randrange(101)}% Cool 😎{ctx.author.mention}", color=nextcord.Color.random())
        await ctx.send(embed=embed)

    @commands.command()
    async def epicgamerrate(self, ctx):
        embed = nextcord.Embed(
            title="epic gamer rate machine",
            description=f"You're are {random.randrange(101)}% epic gamer 😎{ctx.author.mention}", color=nextcord.Color.random())
        await ctx.send(embed=embed)

    #EIGHT BALL
    @commands.command(aliases=['8ball', '8b'])
    async def eightball(self, ctx, *question):
        responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                     "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
                     "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
                     "Yes.", "Yes – definitely.", "You may rely on it."]

        await ctx.send(f":8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}")
