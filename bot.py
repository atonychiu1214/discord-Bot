from click import command
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('OTUwOTkxOTAxOTQxNzA2Nzky.Yig-OQ.NBlldadlzu4nrx4vIbF3zoodizE')