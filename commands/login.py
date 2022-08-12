from discord.ext import commands
import discord
import os

class Login(commands.Cog):
    """Works with logins"""
    def __init__(self,bot) :
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        channel = self.bot.get_channel(1006418619871268985)
        if message.channel == channel:
            msg = str(message.content)
            await discord.Member.edit(message.author,nick=msg)
            guild = self.bot.get_guild(1004178112235450428)
            roleidnovato = 1006418861463187467
            roleidmembro = 1004235156489519207
            roleremove = guild.get_role(roleidnovato)
            roleadd = guild.get_role(roleidmembro)
            await discord.Member.add_roles(message.author,roleadd)
            await discord.Member.remove_roles(message.author,roleremove)

            
def setup(bot):
    bot.add_cog(Login(bot))
