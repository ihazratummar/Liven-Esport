# region imports <- This is foldable
import discord
from client import bot
from dotenv import load_dotenv
import requests
import os
from admin_commands import *
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
