from discord.ext import commands, tasks

class Clean(commands.Cog):
    """Work with Clean Messages"""
    def __init__(self,bot) :
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.clean.start()

    @tasks.loop(minutes=10)
    async def clean(self):
        channel = self.bot.get_channel(1006418619871268985)
        if channel:
            await channel.purge(limit=100)

def setup(bot):
    bot.add_cog(Clean(bot))
