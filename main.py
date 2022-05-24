import discord
from discord.ext import commands
import random, string
import os
#settings

admins = []   #can use serverlist command
cooldown = 5     # in seconds
nocooldown= [] # no cooldown
prefix = "."  # prefix of the bot
amount_per_command = 50  # how much codes bot sends per command
amount_txt = 500
invite = "" # bot invite
supportserver = "" # ur supportserver
token = "token"  # bot token

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
@bot.event
async def on_ready():
 print("ready")
 activity = discord.Game(name=f"Prefix: {prefix} ", type=3)
 await bot.change_presence(status=discord.Status.online, activity=activity)



@bot.command()
async def servercount(ctx):
 count = 0
 for server in bot.guilds:
  count += 1
 await ctx.send(f"I am in {count} Servers!")



@bot.command()
@commands.cooldown(1, cooldown, commands.BucketType.member)
async def nitro(ctx):
  if ctx.author.id in nocooldown:
   nitro.reset_cooldown(ctx)
  embed = discord.Embed(color=16379747, description=f'I have sent you {amount_per_command} unchecked nitro codes. Check your dms!')
  await ctx.send(embed=embed)
  for i in range(amount_per_command):
   code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
   dm = await ctx.author.create_dm()
   await dm.send(f"https://discord.gift/{code}\n")

@bot.command()
@commands.cooldown(1, cooldown, commands.BucketType.member)
async def nitrotxt(ctx):
  with open("codes.txt", "w") as f:
    if ctx.author.id in nocooldown:
      nitrotxt.reset_cooldown(ctx)
    embed = discord.Embed(color=16379747, description=f'I have sent you {amount_txt} unchecked nitro codes in a txt. Check your dms!')
    for _ in range(amount_txt):
      code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
      f.write(f"https://discord.gift/{code}\n")
    f.close()
    dm = await ctx.author.create_dm()
    await dm.send(file=discord.File("codes.txt"))
    embed = discord.Embed(color=16379747, description=f'I have sent you {amount_txt} unchecked nitro codes as txt. Check your dms!')
    await ctx.send(embed=embed)
    os.remove("codes.txt")


@bot.command()
async def serverlist(ctx):
 if ctx.author.id in admins:
  embed = discord.Embed(color=0xffbc00, title="Serverlist")
  for server in bot.guilds:
   embed.add_field(name=f"{server}", value=server.id)
  await ctx.send(embed=embed)

@bot.command()
async def support(ctx):
  await ctx.send(supportserver)



@bot.command()
async def invite(ctx):
  await ctx.channel.send(invite)

@bot.command()
async def nhelp(ctx):
 embed = discord.Embed(color=0xffbc00, title="Help")
 embed.add_field(name=f"{prefix}nitro", value=f"Sends {amount_per_command} unchecked nitro codes", inline=False)
 embed.add_field(name=f"{prefix}nitrotxt", value=f"Sends {amount_txt} unchecked nitro codes as txt")
 embed.add_field(name=f"{prefix}support", value=f"Sends our support server invite")
 embed.add_field(name=f"{prefix}invite", value=f"Sends invite to invte our bot")
 embed.add_field(name=f"{prefix}nhelp", value="Shows this Help Page.", inline=False)
 embed.add_field(name=f"{prefix}servercount", value="Shows in how many server I am.", inline=False)
 await ctx.send(embed=embed)

@nitro.error
async def nitro_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
     logembed1 = discord.Embed(color=0x3498db, description=error)
     await ctx.send(embed=logembed1)

bot.run(token)
