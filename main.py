import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
from keep_alive import keep_alive
from wish_gen import generateWishes
import asyncio

tokenId = os.environ['TOKEN']
client = discord.Client()

#Prefix
client = commands.Bot(command_prefix = '+')

@client.event
#Will print "bot online" in the console when the bot is online
async def on_ready():
  print("keqoooooooong") 

@client.command()
async def wish(ctx):
    wishNumber = 0
    embed=discord.Embed(title="🌠 Genshin Wish Simulator 🌠", description="IM A TRAIN", color=0x3ba4eb)
    embed.description = generateWishes()


    message = await ctx.send(embed=embed)


#Runs web server
keep_alive()

client.run(tokenId)