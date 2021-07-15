import configparser
import discord
from discord import role
from discord.ext import commands

config = configparser.ConfigParser()
config.read("config.ini")

role_spanjool_id = int(config['Roles']['R_SPANJOOL_ID'])
role_burgerij_id = int(config['Roles']['R_BURGERIJ_ID'])
role_ridder_id = int(config['Roles']['R_RIDDER_ID'])
roles_removable_ids = [role_spanjool_id, role_burgerij_id, role_ridder_id]
debug_channel_id = int(config['Debug']['OUTPUT_CHANNEL_ID'])
context = None

class FeatureTest(commands.Cog):
    def __init__(self, client):
        self.client = client

    def getMemberRoles(self, member: discord.Member):
        return member.roles
    
    def checkMemberHasRole(self, member: discord.Member, role_name):
        if role_name in member.roles:
            return True
        else:
            return False

    async def setRoles(self, member: discord.Member, roles):
        await member.add_roles(roles)

    async def removeRoles(self, member: discord.Member, roles):
        await member.remove_roles(roles)

    @commands.Cog.listener() #event decorator for inside cogs
    async def on_ready(self):
        print(f"Cog FeatureTest initialized")

    @commands.command(aliases=['test'])
    async def ping(self, ctx):
         debug_channel = self.client.get_channel(debug_channel_id)
         await debug_channel.send("hi!")

    @commands.command(aliases=['guildroles'])
    async def getGuildRoles(self, ctx):
        guild = ctx.guild
        debug_channel = self.client.get_channel(debug_channel_id)
        await debug_channel.send(f"Roles: {guild.roles}")

    









def setup(client):
    client.add_cog(FeatureTest(client))
