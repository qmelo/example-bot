import discord
from discord import app_commands
from settings import DISCORD_BOT_TOKEN

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('pong')
    
@bot.event
async def on_ready():
    await tree.sync()
    
bot.run(DISCORD_BOT_TOKEN)