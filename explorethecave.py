import time

import gspread
from discord import Embed
from discord.ext.commands import BucketType, cooldown

import bank
import cavedata
from appconf import conf
from context_ext import is_channel_allowed
from discord_bot import bot

caves = cavedata.load_cave_data()


@bot.command(pass_context=True)
@cooldown(1, conf.cooldowns.cave, BucketType.user)
async def cave(ctx):
    if is_channel_allowed(ctx):
        random_cave = caves.random()
        await ctx.send(Embed(
            description=f"{ctx.message.author.mention} is exploring the BΞASTCAVE!",
            color=(0x05ff76),
            url=random_cave.gifLink,
        ))
        channel = bot.get_channel(conf.add_money_channel)

        reward = random_cave.reward
        if reward != None:
            if reward.cash != None:
                await channel.send(f" {ctx.message.author.mention}" + " found <a:Coin:938866055831507034> {reward.cash} in the Cave!")
                bank.reward_cash(
                    user_id=ctx.message.author.id,
                    cash=reward.cash
                )
            elif reward.item != None:
                await channel.send(f" {ctx.message.author.mention}" + " found the **{reward.item}**, collect all 3.")


@ bot.command(pass_context=True)
@ cooldown(1, conf.cooldowns.ticket, BucketType.user)
async def claim(ctx):
    if is_channel_allowed(ctx):
        await ctx.send(embed=Embed(
            description=f"{ctx.message.author.mention} claimed a weekly beastticket!",
            color=(0x05ff76)
        ))
        channel = bot.get_channel(conf.add_money_channel)
        await channel.send(
            f" {ctx.message.author.mention}" +
            " claimed a weekly BEASTTICKET and got <a:Coin:938866055831507034> 60.000 added to balance!"
        )
        bank.reward_cash(user_id=ctx.message.author.id)


@ bot.command(pass_context=True)
async def ticket(ctx):
    if is_channel_allowed(ctx):
        balance = bank.get_balance(user_id=ctx.message.author.id)
        if balance >= 60000:
            bank.buy_ticket(user_id=ctx.message.author.id)
            username = f"{ctx.message.author}"
            userid = f"{ctx.message.author.id}"
            timeconversion = list(time.ctime().split(" "))
            date = str(timeconversion[1:4]).replace(
                "[", "").replace("'", "").replace(",", "").replace("]", "")
            print(username + date + userid)
            updatesheet(username, date, userid)
            await ctx.send(embed=Embed(
                description=f"{ctx.message.author.mention} purchased a BEASTTICKET!",
                color=(0x05ff76)
            ))
            channel = bot.get_channel(conf.add_money_channel)
            await channel.send(f" {ctx.message.author.mention}" + " purchased a BEASTTICKET and spend <a:Coin:938866055831507034> 60.000 for it!")
        else:
            await ctx.send(embed=Embed(
                description=f"{ctx.message.author.mention} **Not enough <a:Coin:938866055831507034> BEASTCOINS for a BEASTTICKET**",
                color=(0xff0505)
            ))


sa = gspread.service_account(filename="service_account.json")
sh = sa.open("EPICBEAST TICKETS")
worksheet = sh.worksheet("BEASTTICKETS")


def updatesheet(username, date, userid):
    index = worksheet.acell("F1").value
    ticketindex = int(index) - 1
    worksheet.update(f"A{index}:D{index}", [
                     [ticketindex, username, date, userid]])
    newindex = int(index) + 1
    worksheet.update("F1", f"{newindex}")
    return


# make sure to only start when this python file is executed
if __name__ == '__main__':
    bot.run(conf.tokens.discord)
