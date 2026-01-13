import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(
    command_prefix="s.",
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print(f"{bot.user} está online!")

@bot.command()
async def help(ctx):
    await ctx.send(
        f"Olá, {ctx.author.mention}! "
        "Sou a **Sophia**, a bot inspirada na Sophia do Katseye. "
        "Meu prefixo é `s.`, fácil, né?"
    )

@bot.command()
async def sophia(ctx):
    await ctx.send(file=discord.File("banner.png"))

bot.run(os.getenv("DISCORD_TOKEN"))
#deploy