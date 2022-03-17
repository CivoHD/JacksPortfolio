
import nextcord
from nextcord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import random





bot = commands.Bot(command_prefix="!")


@bot.command()
async def gif(ctx,*,q="Smile"):

    api_key = "xkOC28aqoUjFgyxGxuyXl5vcEfbTbLmL"
    api_instance = giphy_client.DefaultApi()

    try:

        api_responce = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst =list(api_responce.data)
        giff = random.choice(lst)

        embed = nextcord.Embed(title=q)
        embed.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")

        await ctx.channel.send(embed=embed)

    except ApiException as r:
        print("Exeption for the api")

bot.run("ODkyNTA0MTEwNzA2ODUxODYw.YVN3OQ.bYlXVkHrx0NEJiRL471_FKLf6qU")
