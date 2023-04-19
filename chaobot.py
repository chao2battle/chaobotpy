from discord.ext import commands
import discord



bot = commands.Bot(command_prefix='c-', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Chao!")

@bot.command()
async def chao(ctx):
    await ctx.send("Chao!")

#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#
#    if message.content.startswith('chao') or message.content.startswith('Chao'):
#        await message.channel.send('Chao')


bot.run(BOT_TOKEN)
