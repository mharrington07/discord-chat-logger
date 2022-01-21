import discord
from discord.ext import commands
from discord_slash import SlashCommand


bot = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)


#Events
@bot.event
async def on_ready():
    print("Ready!")

@bot.event
async def on_message(message: str):
  with open("logs.txt", "a") as text_file:
    print(f"{message.author}: {message.content}", file=text_file)

#Varibles
guild_ids = [INSERT GUILD ID HERE]
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)
guild = client.get_guild(INSERT GUILD ID HERE)


#Commands
@slash.slash(name="ping", description='🏓Latency between discord and The bot', guild_ids=guild_ids)
async def _ping(ctx):
  embed=discord.Embed(
    title='**Latency**',
    description=f"🏓**Pong! {round(bot.latency*1000)}ms**",
    color=discord.Color.blurple())
  await ctx.send(embed=embed)



bot.run('INSERT BOT TOKEN HERE')