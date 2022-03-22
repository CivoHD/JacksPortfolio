
from io import BytesIO
import nextcord
from nextcord.ext import commands
from PIL import Image
from Cogs.Utility import utility
from Cogs.Fun import fun
from Cogs.Games import games
from Cogs.Reddit import reddit
from Cogs.API import api
from Cogs.Admin import admin
from Cogs.Roles import roles


client = commands.Bot(command_prefix="!")

client.add_cog(utility(client))
client.add_cog(fun(client))
client.add_cog(games(client))
client.add_cog(reddit(client))
client.add_cog(api(client))
client.add_cog(admin(client))
client.add_cog(roles(client))


#Select option make it edit the embed



@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game(name="c! for de help"))
    print('Im Ready')
    
@client.command(pass_context=True)
async def botservers(ctx):
    await ctx.send("I'm in " + str(len(client.guilds)) + " servers")   

@client.command()
async def owner(ctx):
    await ctx.send('''The creator of this bot is Civo''')




    
    


#@client.command()
#async def hello(ctx):
    #button = Button(label="Click me!", style=nextcord.ButtonStyle.gray)

    #async def button_callback(interaction):
        #await interaction.response.send_message("Hi!")

    #button.callback = button_callback

    #view = View()
    #view.add_item(button)

    #await ctx.send("Hi", view=view)






client.run("ODkzODc2MTI0MDI5OTUyMDMw.YVh1Aw.6WZUr90ifxCP1h1embYrrd8H_V8")
