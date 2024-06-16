import discord
from discord.ext import commands
from points import calc_points as cp
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

@bot.command(name="points", help="test points")
async def points(ctx, *, message):
# Convert the numbers to integers
    try:
        user_pick = [int(num) for num in message.split(" ")]
        if (max(user_pick) > 6):
            raise ValueError
        await ctx.send(f'Your Combination would result in {cp(user_pick)}')
    except ValueError:
        await ctx.send("Only numbers from 1 - 6 are valid.")
        return

bot.run(secrets["TOKEN"])