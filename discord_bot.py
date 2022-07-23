import time

from discord.ext.commands import Bot, CommandOnCooldown
from discord import Intents, Embed
from appconf import conf

bot = Bot(
    command_prefix=conf.command_prefix,
    intents=Intents(members=True)
)


@bot.event
async def on_ready():
    print('Bot successfully logged in as {0.user}'.format(bot))


@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, CommandOnCooldown):
        cooldown_time = (f"{error.retry_after:.0f}")
        int_time = int(cooldown_time)
        time_converted = time.strftime(
            '**%H hours %M minutes %S seconds**', time.gmtime(int_time))
        days = int_time / 86400
        await ctx.send(embed=Embed(
            description=f"**You are still on cooldown** {ctx.message.author.mention}, try again in **{int(days)} days** {str(time_converted)} !",
            color=(0xff0505)
        ))

if __name__ == "__main__":
    bot.run(conf.tokens.discord)
