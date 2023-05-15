# region imports <- This is foldable
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import app_commands
from client import *
from dotenv import load_dotenv
import os
import admin_commands
import user_commands

# endregion


load_dotenv()
token = os.getenv("token")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is now ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)

bot.run(token)