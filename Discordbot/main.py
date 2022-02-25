import nextcord
from nextcord.ext import commands
from fun_commands import funCommands
from Truths_or_dares import TruthorDare
from Dad_Jokes import dadCommands
from google_image import googleImage
from actionsGIFS import ActionGifs
from help_Command import helpCommand


client = commands.Bot(command_prefix="!")
client.remove_command('help')

client.add_cog(funCommands(client))
client.add_cog(TruthorDare(client))
client.add_cog(dadCommands(client))
client.add_cog(googleImage(client))
client.add_cog(ActionGifs(client))
client.add_cog(helpCommand(client))


@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game(name="!help"))
    print('Im Ready')


client.run("OTQ2NTM3MTY4NzQ5MzMwNDky.YhgJbg.swhgx62g6PaZRohzDonIHVgc6xk")
