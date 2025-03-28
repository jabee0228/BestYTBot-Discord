import discord
from discord.ext import commands
import json
from bot import MyBot
from commands import setup_commands
import os

if not os.path.exists("../music_temp"):
    os.makedirs("../music_temp")

with open("../config/config.json", "r") as config_file:
    config = json.load(config_file)
TOKEN = config["TOKEN"]

bot = MyBot()
setup_commands(bot)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("The bot is online")

bot.run(TOKEN)
