import discord
from discord.ext import commands
import random

class Decision:
    def __init__(self, bot):
        self.bot = bot

    def answer(self, ctx):
        num = random.randint(0,100)
        if num >= 50:
            msg = "Nope"
        else:
            msg = "Yep"
        main = f"{ctx.author.mention} rolled: {num}\nAnswer: {msg}"
        await ctx.send(main)
        

def setup(bot):
    bot.add_cog(Decision(bot))