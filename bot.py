import discord
from discord.ext import commands

TOKEN = "MTM3OTUxMzA3NjE4OTEwNjI2OA.GPLCM-.0r05FZP89-EA1Mymced1cuwxB74SO_ehSEUwdc"  # Ersetze mit deinem Token

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
