import nextcord
from nextcord.ext import commands


class roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def addrole(self, ctx, role: nextcord.Role = None, member: nextcord.Member = None):
        if role == None:
            return await ctx.send("Please mention a role!")
        elif member == None:
            return await ctx.send("Please mention a member")
        await member.add_roles(role)
        embed = nextcord.Embed(
            title="Role added!", description=f"Added the **{role}** to {member.mention}", timestamp=ctx.message.created_at, color=nextcord.Color.random())
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def removerole(self, ctx, role: nextcord.Role = None, member: nextcord.Member = None):
        if role == None:
            return await ctx.send("Please mention a role!")
        elif member == None:
            return await ctx.send("Please mention a member")
        await member.remove_roles(role)
        embed = nextcord.Embed(
            title="Role Removed!", description=f"Removed the **{role}** role from {member.mention}", timestamp=ctx.message.created_at, color=nextcord.Color.random())
        await ctx.send(embed=embed)
