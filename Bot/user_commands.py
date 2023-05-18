# region imports <- This is foldable
import discord
from client import bot
from discord.ext import commands
from discord.ext.commands import check
import requests
import os

# endregion


@bot.tree.command(name="ping", description="ping server")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {bot.latency * 1000:.2f}ms")


@bot.tree.command(name="enroll", description="enrols a user to the server")
async def enroll(interaction: discord.Interaction):
    link = "https://forms.gle/vBm5VpfPaExjrAm56"
    await interaction.response.send_message(
        f"Enroll by clicking the link below:\n{link}"
    )
