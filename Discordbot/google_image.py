import nextcord
import random
from nextcord.ext import commands
from googleapiclient.discovery import build

api_key = "AIzaSyAUdBQkgvteZ7Anv5cWgYsP0uBdHc0tcBU"


class googleImage(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def showpic(self, ctx, *, search):
        ran = random.randint(0, 9)
        resources = build("customsearch", "v1", developerKey=api_key).cse()
        result = resources.list(
            q=f"{search}", cx="c10523b00e37d5acc", searchType="image"
        ).execute()
        url = result["items"][ran]["link"]
        embed1 = nextcord.Embed(title=f"Here your image ({search.title()})")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)
