import discord
from discord.ext import commands
import random

class Random:
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Random(bot))