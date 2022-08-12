from discord.ext import commands, tasks
import datetime

class Dates(commands.Cog):
    """Work with date"""
    def __init__(self,bot) :
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        #self.current_time.start()
        ...


    @tasks.loop(seconds=10)
    async def current_time(self):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel(1006418619871268985)

        await channel.send("Data atual: " + now)

def setup(bot):
    bot.add_cog(Dates(bot))
