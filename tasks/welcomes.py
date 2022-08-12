from discord.ext import commands, tasks
import discord
import os

class Welcome(commands.Cog):
    """Work with welcomes messages"""
    def __init__(self,bot) :
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.welcome.start()
        


    @tasks.loop(minutes=5)
    async def welcome(self):
        channel = self.bot.get_channel(1006418619871268985)
        if channel:
            embed = discord.Embed(
            title="LifeInvader",
            description="Seja Muito Bem Vindo à Maior Organização de Lavagem do ATENAS!",
            color=0xD44D4A,
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Feito por: Reiifer Luiz | 6135", icon_url=self.bot.user.avatar_url)
        embed.set_image(url="https://static.wikia.nocookie.net/gtawiki/images/d/df/LifeinvaderOffice-GTAV.png/revision/latest?cb=20130917013108")
        embed.add_field(name="Salários",value="Possuímos o melhor salário da cidade!")
        embed.add_field(name="Parcerias",value="Temos parceria com praticamente todas as organizações da cidade!")
        embed.add_field(name="Ascenção",value="Possibilidade de Ascenção de Cargo!")
        embed.add_field(name="Regras",value=f"- Estar no Rádio Sempre! {os.linesep}- Estar Devidamente Uniformizado! {os.linesep}- Respeitar Estritamente a Hierarquia!",inline=False)
        embed.add_field(name="Identificação no Discord",value=f"Digite seu nome nesse formato:{os.linesep}```- Nome do Jogo | ID do Jogo```",inline=False)
        channel = self.bot.get_channel(1006418619871268985)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Welcome(bot))
