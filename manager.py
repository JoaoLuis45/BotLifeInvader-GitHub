from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, CommandInvokeError

class Manager(commands.Cog):
    """Manager the bot"""
    def __init__(self,bot) :
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou pronto como: {self.bot.user}')
        #current_time.start()


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, CommandNotFound):
            await ctx.send('Comando inexistente, Confira a lista de comandos usando o !help')
        elif isinstance(error, CommandInvokeError):
            await ctx.send('O comando requer dois ou mais argumentos, preencha-o corretamente!')
        else:
            raise error



def setup(bot):
    bot.add_cog(Manager(bot))
