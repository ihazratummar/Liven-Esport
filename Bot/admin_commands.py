# region imports <- This is foldable 
import discord
from client import bot
from discord.ext import commands
from discord.ext.commands import check
from discord import app_commands
import requests
import os
#endregion

@bot.tree.command(name="kick", description="kick a member")
@app_commands.checks.has_permissions(administrator=True)
async def kick(interact: discord.Interaction, member: discord.Member):
    await interact.response.defer()
    await member.kick()
    await interact.response.send_message(f"{user.name} has been kicked by {interaction.user.name}")
    
@kick.error
async def kick_error(interartion: discord.Interaction, error):
    await interartion.response.send_message(f"Hey {interartion.user.name}! This ia an admin only command.")
    
@bot.tree.command(name="say", description="say something")
@app_commands.checks.has_permissions(administrator=True)
async def say(interact: discord.Interaction, *, message: str):
    await interact.response.send_message(message)
    
@say.error
async def say_error(interartion: discord.Interaction, error):
    await interartion.response.send_message(f"Hey {interartion.user.name}! This ia an admin only command.")