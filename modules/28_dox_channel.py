# pip install discord.py
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def dox(ctx, user: discord.User):
    await ctx.send(f"Doxing {user.name}#{user.discriminator}")

bot.run('YOUR_TOKEN_HERE')