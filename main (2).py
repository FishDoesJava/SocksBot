#Imports
import discord,os
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions#, CheckFailure

#Global vars
intents = discord.Intents.default()
intents.members=True
token = os.getenv("bot_token")
bot_name = "SocksBot"
cmd_prefix = "!"
#mod_role = "Moderator"

client = commands.Bot(command_prefix = cmd_prefix,intents=intents)
client.remove_command('help')

#Events & Commands
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Streaming(name=f"SunnySocks", url="https://www.twitch.tv/sunnysocks"))
  print("Wake up, Em! It's time to code!")

@client.event
async def on_member_join(member):
  channel = client.get_channel(1032202597626556557)
  embed = discord.Embed(
    title = f"Welcome {member.name}",
    description = f"Thanks for joining {member.guild.name}!",
    colour = discord.Colour.green()
  )

  embed.set_footer(text = "read #rules to get started!")
  embed.set_thumbnail(url=member.display_avatar)
  await channel.send(embed=embed)
  
@client.command()
async def help(ctx):
  embed = discord.Embed(
    title = 'Help',
    description = "Try out these commmands below",
    colour = discord.Colour.green()
  )

  embed.set_footer(text = "remember to delete this text later.")
  embed.set_author(name = bot_name)
  embed.add_field(name = f"{cmd_prefix}ping", value = "Check Ping",inline = False)
  await ctx.send(embed=embed)  
  
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def theresnowaythatanotherbothasthiscommand(ctx):
  await ctx.send(f'MEE6 SUCKS')

client.run(token)