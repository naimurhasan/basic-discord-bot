import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have successfully logged in as {0.user.name}'.format(client))

@client.command()
async def ping(ctx):
    """Say pong"""
    await ctx.send('Pong [{}ms]'.format(round(client.latency*1000, 1)))

@client.command()
async def introduce(ctx):
    """I'll introduce myself"""
    await ctx.send('Hey, I\'m a discrod bot! Made by Naimur&Arefin.')

client.run('')

