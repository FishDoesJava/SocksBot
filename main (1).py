import discord, os
from discord.ext import commands

#Global vars
bot_name = "Andy Himself"
cmd_prefix = "!"
mod_role = "Managers"

client = commands.Bot(command_prefix=cmd_prefix)
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(
        name=f"just imagine this is something funny"))
    print("Andy has Arisen")


@client.command()
async def help(ctx):
    embed = discord.Embed(title='Help',
                          description="Try out these commmands below",
                          colour=discord.Colour.orange())

    embed.set_footer(text="remember to delete this text later.")
    embed.set_author(name=bot_name)
    embed.add_field(
        name=f"{cmd_prefix}seasonal",
        value="Check All Andy's Seasonal Treats and Their Availablity",
        inline=False)
    embed.add_field(name=f"{cmd_prefix}ping", value="Check Ping", inline=False)
    embed.add_field(name=f"{cmd_prefix}sales",
                    value="Check Weekly Gross Sales by the Hour",
                    inline=False)
    embed.add_field(name=f"{cmd_prefix}labor",
                    value="Not yet implemented",
                    inline=False)
    await ctx.send(embed=embed)


@client.command()
async def seasonal(ctx):
    embed = discord.Embed(
        title='Seasonal Items',
        description="Andy's Seasonal Treats and Their Availability",
        colour=discord.Colour.random())

    embed.set_footer(text="Actual availability times may vary.")
    embed.set_author(name=bot_name)
    embed.add_field(name=f"Cookie Casanova Jackhammer™",
                    value="Available mid January",
                    inline=False)
    embed.add_field(name=f"Cookie Casanova Sundae",
                    value="Available mid January",
                    inline=False)
    embed.add_field(name=f"The CrumbleMint Shake",
                    value="Available February",
                    inline=False)
    embed.add_field(name=f"Mint Cookie Concrete",
                    value="Available February",
                    inline=False)
    embed.add_field(name=f"Blueberry Chip Chocolate Concrete",
                    value="Available late April",
                    inline=False)
    embed.add_field(name=f"Strawberry Shortcake Sundae",
                    value="Available late April",
                    inline=False)
    embed.add_field(name=f"Blackberry Concrete",
                    value="Available late April",
                    inline=False)
    embed.add_field(name=f"Peach Concrete",
                    value="Available NOW!",
                    inline=False)
    embed.add_field(name=f"Peach Sundae", value="Available NOW!", inline=False)
    embed.add_field(name=f"Key Lime Pie Concrete",
                    value="Available NOW!",
                    inline=False)
    embed.add_field(name=f"Pumpkin Pie Concrete",
                    value="Available mid-September",
                    inline=False)
    embed.add_field(name=f"S’mores Jackhammer™",
                    value="Available mid-September",
                    inline=False)
    embed.add_field(name=f"“Words Can’t Describe It” Apple Pie Concrete",
                    value="Available mid-September",
                    inline=False)
    embed.add_field(name=f"“Words Can’t Describe It” Apple Pie Sundae",
                    value="Available late November",
                    inline=False)
    embed.add_field(name=f"Andy Nog Shake",
                    value="Available late November",
                    inline=False)
    embed.add_field(name=f"Santa Brownie Jackhammer™",
                    value="Available late November",
                    inline=False)
    embed.add_field(name=f"Santa Brownie Sundae",
                    value="Available late November",
                    inline=False)
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def sales(ctx):
    await ctx.send(file=discord.File(r'Gross Sales by Hour.pdf'))


@client.command()
async def labor(ctx):
    await ctx.send(f'Check back later, That\'s not ready yet!')

@client.command()
async def theresnowaythatanotherbothasthiscommand(ctx):
  await ctx.send(f'MEE6 SUCKS')

client.run(os.getenv("TOKEN"))
