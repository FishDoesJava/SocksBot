import discord,os
from discord.ext import commands
from discord.ext.commands import has_permissions#, CheckFailure
import random
#Global vars
intents = discord.Intents.all()
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
  await client.change_presence(activity=discord.Streaming(name=f"SunnySocks's Official Discord Bot!", url="twitch.tv/sunnysocks"))
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

  embed.set_footer(text = f"More functions on the way!")
  embed.set_author(name = bot_name)
  embed.add_field(name = f"!ping", value = "Issues with the bot? Check its ping!",inline = False)
  embed.add_field(name = f"!chad", value = "Find out how chad you are!",inline = False)
  embed.add_field(name = f"!sus", value = "Find out how SUS you are! ඞ",inline = False)
  await ctx.send(embed=embed)

@client.command()
async def chad(ctx):
  await ctx.send(f'{ctx.author.mention} is {random.randint(1,120)}% chad!')

@client.command()
async def bucket(ctx):
  await ctx.send(file = discord.File('itsbucket.png'))
  await ctx.send(f'It\'s buckèt.')
@client.command()
async def sus(ctx):
  await ctx.send(f'{ctx.author.mention} is {random.randint(1,120)}% SUS ඞ!')
@client.command()
async def rules(ctx):
  embed = discord.Embed(
    title = 'Sunny\'s Rules',
    description = "Please follow the rules so everyone can have a good time in the Discord! :D",
    colour = discord.Colour.green()
  )

  embed.set_footer(text = "Please contact an administrator if there is any confusion!")
  embed.set_author(name = bot_name)
  embed.add_field(name = f"English Only", value = "Please only speak English in text channels!",inline = False)
  embed.add_field(name=f"No Harassment", value = "Please be kind to everyone! :D",inline = False)
  embed.add_field(name=f"No Sharing Personal Information", value = "Sharing your info online is dangerous! Please don't!",inline = False)
  embed.add_field(name=f"Love everyone!", value = "Please no slurs, racism, homophobia, etc!",inline = False)
  embed.add_field(name=f"Be kind!", value = "Please help us keep our server a safe and happy place! :D",inline = False)
  await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def theresnowaythatanotherbothasthiscommand(ctx):
  await ctx.send('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae diam est. Suspendisse eros turpis, tempor in nisi quis, fermentum laoreet lectus. Proin non felis consectetur, commodo purus lacinia, vulputate augue. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent rhoncus hendrerit sem. Pellentesque tristique porta auctor. Duis scelerisque et urna vel ornare.')

@client.command()
async def credits(ctx):
  await ctx.send(f'Developed by <@741413464945197096> and <@338072191457427468>!')
client.run(token)
