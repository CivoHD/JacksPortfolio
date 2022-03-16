from email import header
from aiohttp import request
import nextcord
from nextcord.ext import commands




bot = commands.Bot(command_prefix="!")


@bot.command()
async def truth(ctx):

    url = "https://api.truthordarebot.xyz/v1/truth"

    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(f"**{data['question']}**")
        else:
            await ctx.send(f"{response.status}")

@bot.command()
async def dare(ctx):

    url = "https://api.truthordarebot.xyz/v1/dare"

    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(f"**{data['question']}**")
        else:
            await ctx.send(f"{response.status}")   

@bot.command()
async def nhie(ctx):

    url = "https://api.truthordarebot.xyz/v1/nhie"

    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(f"**{data['question']}**")
        else:
            await ctx.send(f"{response.status}")


@bot.command()
async def wyr(ctx):

    url = "https://api.truthordarebot.xyz/v1/wyr"

    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(f"**{data['question']}**")
        else:
            await ctx.send(f"{response.status}")


bot.run("ODkyNTA0MTEwNzA2ODUxODYw.YVN3OQ.bYlXVkHrx0NEJiRL471_FKLf6qU")
