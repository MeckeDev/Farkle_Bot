import discord
from discord.ext import commands
import json

# Set up the bot with the command prefix #
intents = discord.Intents.default()
intents.message_content = True  # Ensure the bot can read message content
bot = commands.Bot(command_prefix="#", intents=intents)

with open("secrets.json") as f:
    secrets = json.load(f)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.command(name="hello", help="Responds with Hello!")
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(secrets["TOKEN"])