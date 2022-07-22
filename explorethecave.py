import discord
import random
import time
import requests
import os
import gspread
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.members = True
prefix = str(os.environ.get("commandprefix"))
bot = commands.Bot(command_prefix = prefix,intents=intents)
token = str(os.environ.get("token"))

sa = gspread.service_account(filename="service_account.json")
sh = sa.open("EPICBEAST TICKETS")
worksheet = sh.worksheet("BEASTTICKETS")

print ("Tassilo ist der beste, FACT")

guild_id = str(os.environ.get("serverid"))
command_channel = int(os.environ.get("commandchannelid"))
claim_channel = int(os.environ.get("claimchannelid"))
add_money_channel = int(os.environ.get("responsechannelid"))
command_cooldown = int(os.environ.get("cavecooldown")) #in seconds (10800 = 3h)
weekly_cooldown = int(os.environ.get("claimcooldown")) #in seconds (604800 = 7d)

unbversion = "v1"
unbtoken = str(os.environ.get("unbtoken"))

result01 = "https://i.imgur.com/dmdBE7X.gif"
result02 = "https://i.imgur.com/gXox0md.gif"
result03 = "https://i.imgur.com/hViFojP.gif"
result04 = "https://i.imgur.com/H0EFikD.gif"
result05 = "https://i.imgur.com/c1Sy083.gif"
result06 = "https://i.imgur.com/Aqpc4Gh.gif"
result07 = "https://i.imgur.com/nK9hjpx.gif"
result08 = "https://i.imgur.com/fW7KURx.gif"
result09 = "https://i.imgur.com/8CYSIhR.gif"
result10 = "https://i.imgur.com/Rm0cN8x.gif"
result11 = "https://i.imgur.com/CVfAtaz.gif"
result12 = "https://i.imgur.com/3FSl0c3.gif"
result13 = "https://i.imgur.com/RWwJzPV.gif"
result14 = "https://i.imgur.com/BzFYQCK.gif"
result15 = "https://i.imgur.com/gIZTQTr.gif"
result16 = "https://i.imgur.com/9W9V5Wn.gif"
result17 = "https://i.imgur.com/rsThJdn.gif"
result18 = "https://i.imgur.com/wDrN9vv.gif"
result19 = "https://i.imgur.com/xvAFWZg.gif"
result20 = "https://i.imgur.com/IbN56z6.gif"
result21 = "https://i.imgur.com/GCjkoh5.gif"
result22 = "https://i.imgur.com/kuBcGIn.gif"
result23 = "https://i.imgur.com/MWhuwZH.gif"
result24 = "https://i.imgur.com/8YEJlAN.gif"

probability = [
  int(os.environ.get("pCAN")), #CAN
  int(os.environ.get("p25k")), #25k
  int(os.environ.get("pPIZZA")), #PIZZA
  int(os.environ.get("pTICKET")), #TICKET
  int(os.environ.get("pSHROOM")), #SHROOM
  int(os.environ.get("p5k")), #5k
  int(os.environ.get("pUSB")), #USB
  int(os.environ.get("pROCK")), #ROCK
  int(os.environ.get("pSOAP")), #SOAP
  int(os.environ.get("pCONTROLLER")), #CONTROLLER
  int(os.environ.get("pPICKAXE")), #PICKAXE
  int(os.environ.get("p10k")), #10k
  int(os.environ.get("pGAMEBOY")), #GAMEBOY
  int(os.environ.get("pPC")), #PC
  int(os.environ.get("pSOCK")), #SMELLYSOCK
  int(os.environ.get("pPEPE")), #PEPE
  int(os.environ.get("pMOUSE")), #MOUSE
  int(os.environ.get("pDVD")), #DVD
  int(os.environ.get("pHEADSET")), #HEADSET
  int(os.environ.get("pTRI1")), #TRI1
  int(os.environ.get("pTRI2")), #TRI2
  int(os.environ.get("pTRI3")), #TRI3
  int(os.environ.get("p500")), #500
  int(os.environ.get("p1k")) #1k
]

#https://i.imgur.com/dmdBE7X.gif #CAN
#https://i.imgur.com/gXox0md.gif #25k
#https://i.imgur.com/hViFojP.gif #PIZZA
#https://i.imgur.com/H0EFikD.gif #TICKET
#https://i.imgur.com/IbN56z6.gif #TRI1
#https://i.imgur.com/c1Sy083.gif #SHROOM
#https://i.imgur.com/Aqpc4Gh.gif #5k
#https://i.imgur.com/nK9hjpx.gif #USB
#https://i.imgur.com/fW7KURx.gif #ROCK
#https://i.imgur.com/8CYSIhR.gif #SOAP
#https://i.imgur.com/kuBcGIn.gif #TRI3
#https://i.imgur.com/CVfAtaz.gif #PICKAXE
#https://i.imgur.com/3FSl0c3.gif #10k
#https://i.imgur.com/RWwJzPV.gif #GAMEBOY
#https://i.imgur.com/BzFYQCK.gif #PC
#https://i.imgur.com/gIZTQTr.gif #SMELLYSOCK
#https://i.imgur.com/9W9V5Wn.gif #PEPE
#https://i.imgur.com/rsThJdn.gif #MOUSE
#https://i.imgur.com/GCjkoh5.gif #TRI2
#https://i.imgur.com/wDrN9vv.gif #DVD
#https://i.imgur.com/xvAFWZg.gif #HEADSET
#https://i.imgur.com/Rm0cN8x.gif #CONTROLLER
#https://i.imgur.com/MWhuwZH.gif #500
#https://i.imgur.com/8YEJlAN.gif #1k

result = [
  result01,
  result02,
  result03,
  result04,
  result05,
  result06,
  result07,
  result08,
  result09,
  result10,
  result11,
  result12,
  result13,
  result14,
  result15,
  result16,
  result17,
  result18,
  result19,
  result20,
  result21,
  result22,
  result23,
  result24
]

@bot.event
async def on_ready():
  print('Bot successfully logged in as {0.user}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    cooldown_time = (f"{error.retry_after:.0f}")
    int_time = int(cooldown_time)
    time_converted = time.strftime('**%H hours %M minutes %S seconds**', time.gmtime(int_time))
    days = int_time / 86400
    em = discord.Embed(description = (f"**You are still on cooldown** {ctx.message.author.mention}, try again in **{int(days)} days** " + str(time_converted) + "!"), color = (0xff0505))
    await ctx.send(embed=em)

payload = {
    "reason": "Cave reward",
    "cash": 0
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": unbtoken
}

@bot.command(pass_context = True)
@commands.cooldown(1,command_cooldown,commands.BucketType.user)
async def cave(ctx):
  channel = ctx.channel.id
  restricted_channels = [command_channel]
  if channel in restricted_channels:
    preselection = (random.choices(result, probability))
    selection = str(preselection).replace('[','').replace(']','').replace('\'','')
    embed = discord.Embed(description = (f"{ctx.message.author.mention} is exploring the BΞASTCAVE!"), color = (0x05ff76))
    embed.set_image(url=selection)
    await ctx.send(embed = embed)
    channel = bot.get_channel(add_money_channel)
    if selection == result02:
      payload = {"reason": "Cave reward","cash": 25000}
      await channel.send(f" {ctx.message.author.mention}" + " found <a:Coin:938866055831507034> 25.000 in the Cave!")
      await requests.patch(f"https://unbelievaboat.com/api/{unbversion}/guilds/{guild_id}/users/{ctx.message.author.id}", json=payload, headers=headers)
    if selection == result04:
      payload = {"reason": "Cave reward","cash": 60000}
      await channel.send(f" {ctx.message.author.mention}" + " found <a:Coin:938866055831507034> 60.000 in the Cave!")
      await requests.patch(f"https://unbelievaboat.com/api/{unbversion}/guilds/{guild_id}/users/{ctx.message.author.id}", json=payload, headers=headers)
    if selection == result06:
      payload = {"reason": "Cave reward","cash": 5000}
      await channel.send(f" {ctx.message.author.mention}" + " found <a:Coin:938866055831507034> 5.000 in the Cave!")
      await requests.patch(f"https://unbelievaboat.com/api/{unbversion}/guilds/{guild_id}/users/{ctx.message.author.id}", json=payload, headers=headers)
    if selection == result12:
      payload = {"reason": "Cave reward","cash": 10000}
      await channel.send(f" {ctx.message.author.mention}" + " found <a:Coin:938866055831507034> 10.000 in the Cave!")
      await requests.patch(f"https://unbelievaboat.com/api/{unbversion}/guilds/{guild_id}/users/{ctx.message.author.id}", json=payload, headers=headers)
    if selection == result20:
      await channel.send(f" {ctx.message.author.mention}" + " found the **TRIFORCE OF POWER**, collect all 3.")
    if selection == result21:
      await channel.send(f" {ctx.message.author.mention}" + " found the **TRIFORCE OF WISDOM**, collect all 3.")
    if selection == result22:
      await channel.send(f" {ctx.message.author.mention}" + " found the **TRIFORCE OF COURAGE**, collect all 3.")
    if selection == result23:
      payload = {"reason": "Cave reward","cash": 500}
      await channel.send(f" {ctx.message.author.mention}" + " found <a:Coin:938866055831507034> 500 in the Cave!")
      await requests.patch(f"https://unbelievaboat.com/api/{unbversion}/guilds/{guild_id}/users/{ctx.message.author.id}", json=payload, headers=headers)
    if selection == result24:
      payload = {"reason": "Cave reward","cash": 1000}
      await channel.send(f" {ctx.message.author.mention}" + " found <a:Coin:938866055831507034> 1.000 in the Cave!")
      await requests.patch(f"https://unbelievaboat.com/api/{unbversion}/guilds/{guild_id}/users/{ctx.message.author.id}", json=payload, headers=headers)
    else:
      return
  else:
    return

@bot.command(pass_context = True)
@commands.cooldown(1,weekly_cooldown,commands.BucketType.user)
async def claim(ctx):
  channel = ctx.channel.id
  restricted_channels = [claim_channel]
  if channel in restricted_channels:
    embed = discord.Embed(description = (f"{ctx.message.author.mention} claimed a weekly beastticket!"), color = (0x05ff76))
    payload = {"reason": "Weekly claim","cash": 60000}
    await ctx.send(embed = embed)
    channel = bot.get_channel(add_money_channel)
    await channel.send(f" {ctx.message.author.mention}" + " claimed a weekly BEASTTICKET and got <a:Coin:938866055831507034> 60.000 added to balance!")
    await requests.patch(f"https://unbelievaboat.com/api/{unbversion}/guilds/{guild_id}/users/{ctx.message.author.id}", json=payload, headers=headers)
  else:
    return
    
def stringToList(splitter):
    listRes = list(splitter.split(","))
    return listRes

def stringToList2(splitter2):
    listRes2 = list(splitter2.split(" "))
    return listRes2

def updatesheet(username, date, userid):
  index = worksheet.acell("F1").value
  ticketindex = int(index) - 1
  worksheet.update(f"A{index}:D{index}", [[ticketindex, username, date, userid]])
  newindex = int(index) + 1
  worksheet.update("F1", f"{newindex}")
  return


@bot.command(pass_context = True)
async def ticket(ctx):
  channel = ctx.channel.id
  restricted_channels = [claim_channel]
  if channel in restricted_channels:
    getbalance = requests.get(f"https://unbelievaboat.com/api/{unbversion}/guilds/{guild_id}/users/{ctx.message.author.id}", headers=headers)
    apibalance = str(getbalance.text)
    userbalance = str(stringToList(apibalance)[2]).replace('"cash":','')
    print(userbalance)
    if int(userbalance) > 60000:
      payload = {"reason": "Ticket buy","cash": -60000}
      requests.patch(f"https://unbelievaboat.com/api/{unbversion}/guilds/{guild_id}/users/{ctx.message.author.id}", json=payload, headers=headers)
      username = f"{ctx.message.author}"
      userid = f"{ctx.message.author.id}"
      timeconversion = stringToList2(time.ctime())
      date = str(timeconversion[1:4]).replace("[","").replace("'","").replace(",","").replace("]","")
      print(username + date + userid)
      updatesheet(username, date, userid)
      embed = discord.Embed(description = (f"{ctx.message.author.mention} purchased a BEASTTICKET!"), color = (0x05ff76))
      await ctx.send(embed = embed)
      channel = bot.get_channel(add_money_channel)
      await channel.send(f" {ctx.message.author.mention}" + " purchased a BEASTTICKET and spend <a:Coin:938866055831507034> 60.000 for it!")
    else:
      embed = discord.Embed(description = (f"{ctx.message.author.mention} **Not enough <a:Coin:938866055831507034> BEASTCOINS for a BEASTTICKET**"), color = (0xff0505))
      await ctx.send(embed = embed)
      return
  else:
    return


bot.run(token)