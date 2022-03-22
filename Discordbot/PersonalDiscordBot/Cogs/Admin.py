import datetime
import humanfriendly
import nextcord
from nextcord.ext import commands


#COMMANDS BAN / MUTE / WARN / TIMEOUT / MAKE A NEW FILE TO ASSAIGN ROLES TO USERS

class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        if reason == None:
            reason = " no reason was provided"
        await ctx.guild.kick(member)
        await ctx.send(f"User {member.mention} has been kicked for {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        if reason == None:
            reason = " no reason was provided"
        await ctx.guild.ban(member)
        await ctx.send(f"User {member.mention} has been banned for {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):    
        banned_user = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_user:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} has been unbanned!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member:nextcord.Member, time, *, reason):
        time = humanfriendly.parse_timespan(time)
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
        await ctx.send(f"{member.mention} has been muted because {reason}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: nextcord.Member, *, reason):
        await member.edit(timeout=None)
        await ctx.send(f"{member.mention} has been unmuted because {reason}")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()


    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: nextcord.Member, *, reason):
        await ctx.send(f"{member.mention} you have been warned for {reason}")
