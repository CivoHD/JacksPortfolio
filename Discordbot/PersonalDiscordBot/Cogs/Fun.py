import nextcord
from nextcord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import random

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx, *, q='Stupid'):

        api_key = "xkOC28aqoUjFgyxGxuyXl5vcEfbTbLmL"
        api_instance = giphy_client.DefaultApi()

        try:

            api_responce = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_responce.data)
            giff = random.choice(lst)

            embed = nextcord.Embed(title=q, color=nextcord.Color.random())
            embed.set_image(
                url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")

            await ctx.channel.send(embed=embed)

        except ApiException as r:
            print("Exeption for the api")

