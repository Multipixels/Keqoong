import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from keep_alive import keep_alive
import asyncio
#^ basic imports for other features of discord.py and python ^

tokenId = os.environ['TOKEN']
client = discord.Client()

emojis = ['▶️', '⏩']
imageUrls = ["https://oyster.ignimgs.com/mediawiki/apis.ign.com/genshin-impact/a/a1/Genshin_Impact_20200929215315.jpg?width=1280," ,"https://www.pcinvasion.com/wp-content/uploads/2020/10/Genshin-Impact-wishes-microtransactions-currencies-guide-1a.jpg","https://static1.thegamerimages.com/wordpress/wp-content/uploads/2020/10/Screenshot-2565.png?q=50&fit=crop&w=1920&dpr=1.5" ,"https://www.pcinvasion.com/wp-content/uploads/2020/10/Gen-pct-char-5.jpg" ,"https://s.yimg.com/ny/api/res/1.2/Q3aQzxtxrTn13fsNF_Vrug--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTM1OS45MzM0NDQyNTk1Njc0/https://s.yimg.com/os/creatr-uploaded-images/2021-05/0284e1f0-b15d-11eb-beaf-42b099ca5a0c" ,"https://i.ytimg.com/vi/nZS7cIcWIlw/hqdefault.jpg" ,"https://static1.thegamerimages.com/wordpress/wp-content/uploads/2020/10/pjimage-2020-10-21T120904.306.jpg" ,"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOGMA41vsSPDOCF012lAaHiYiqbAm7prFNcQ&usqp=CAU" ,"https://www.alphr.com/wp-content/uploads/2021/06/Xiao-Wish-Art.jpg" ,"https://cdn.gamerstopia.com/wp-content/uploads/Chonyun-Genshin-Impact-Character-Profile-Featured-Image.jpg"]
fullWishUrl = "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2020/09/genshin-impact-wishes.jpg"

lantern = "\595733537651687426"

#Prefix
client = commands.Bot(command_prefix = '+')

@client.event
#Will print "bot online" in the console when the bot is online
async def on_ready():
  print("keqoooooooong") 

@client.command()
async def wish(ctx):
    wishNumber = 0
    embed=discord.Embed(title="NYOOOOOOOOOOM", description="IM A TRAIN", color=0x3ba4eb)
    embed.set_image(url=imageUrls[wishNumber])
    message = await ctx.send(embed=embed)

    for emoji in emojis:
      await message.add_reaction(emoji)

    def check(reaction, user):
      return user == ctx.author and str(reaction.emoji) == '▶️'

    for loop in range(10):
      try:
        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
      except asyncio.TimeoutError:
        break
      else:
        wishNumber += 1
        newEmbed=embed

        if wishNumber == 10: 
          newEmbed.set_image(url=fullWishUrl)
        else: newEmbed.set_image(url=imageUrls[wishNumber])

        await message.edit(embed=newEmbed)
        await reaction.remove(user)

    newEmbed=embed
    newEmbed.set_image(url=fullWishUrl)
    await message.edit(embed=newEmbed)
    await message.remove_reaction(emojis[0], message.author)
    await message.remove_reaction(emojis[1], message.author)

#Runs web server
keep_alive()

client.run(tokenId) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!