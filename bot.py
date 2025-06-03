import discord
from discord.ext import commands

TOKEN = "."  # Ersetze mit deinem Token

intents = discord.Intents.default()
intents.message_content = True  # Wichtig, sonst funktionieren keine Nachrichten

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

bot.run(TOKEN)
