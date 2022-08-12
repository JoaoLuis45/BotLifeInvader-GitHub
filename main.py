from discord.ext import commands
import discord
from dotenv import load_dotenv
import os

load_dotenv()

bot = commands.Bot("!")
def load_cogs(bot):
    bot.load_extension("manager")
    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")
    for file in os.listdir("tasks"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"tasks.{cog}")


load_cogs(bot)
bot.run(os.environ['token'])


