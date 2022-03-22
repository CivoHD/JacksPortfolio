
from discord import Color
import nextcord
from nextcord.ext import commands


class utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def serverinfo(self, ctx):
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

        serverinfoEmbed = nextcord.Embed(
            timestamp=ctx.message.created_at, color=Color.random())
        serverinfoEmbed.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
        serverinfoEmbed.add_field(name='Member count', value=ctx.guild.member_count, inline=False)
        serverinfoEmbed.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
        serverinfoEmbed.add_field(name='Highest Role', value=ctx.guild.roles[-2], inline=False)
        serverinfoEmbed.add_field(name='Number of roles', value=str(role_count), inline=False)
        serverinfoEmbed.add_field(name='Bots', value=', '.join(list_of_bots), inline=False)
        serverinfoEmbed.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)

        await ctx.send(embed = serverinfoEmbed)


    




