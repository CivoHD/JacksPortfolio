import random
import datetime
import aiohttp
import nextcord
from nextcord.ui import Button, View
from nextcord.ext import commands


class reddit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dankmeme(self, ctx):
        async with ctx.channel.typing():
            async def get_dankmeme():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://www.reddit.com/r/dankmemes.json?sort=hot") as r:
                        dankmeme = await r.json()

                return dankmeme["data"]["children"][random.randint(0, 25)]["data"]["url"]  
                    

            async def button_callback(interaction):
                dankmeme = await get_dankmeme()
                emb = interaction.message.embeds[0].set_image(url=dankmeme)
                await interaction.response.edit_message(embed=emb)

            button1 = Button(label="Next Dankmeme",
                             style=nextcord.ButtonStyle.green, emoji='⏭️')

            view = View()
            button1.callback = button_callback
            view.add_item(button1)

            embed = nextcord.Embed(title="Dankmeme here!")
            embed.set_image(url = await get_dankmeme())
            await ctx.reply(embed=embed, view=view)


            

    @commands.command()
    async def foodporn(self, ctx):
        async with ctx.channel.typing():
            async def get_foodporn():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://www.reddit.com/r/FoodPorn.json?sort=hot") as r:
                        dankmeme = await r.json()

                return dankmeme["data"]["children"][random.randint(0, 25)]["data"]["url"]

            async def button_callback(interaction):
                dankmeme = await get_foodporn()
                emb = interaction.message.embeds[0].set_image(url=dankmeme)
                await interaction.response.edit_message(embed=emb)

            button1 = Button(label="Next foodporn",
                             style=nextcord.ButtonStyle.green, emoji='⏭️')

            view = View()
            button1.callback = button_callback
            view.add_item(button1)

            embed = nextcord.Embed(title="Foodporn here!")
            embed.set_image(url=await get_foodporn())
            await ctx.reply(embed=embed, view=view)



 
