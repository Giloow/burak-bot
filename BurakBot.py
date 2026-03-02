from math import floor
from random import random
from aioconsole import ainput
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    channel = bot.get_channel(1152651843806187662)
    while True:
        content = await ainput('Enter Line')
        await channel.send(content)


@bot.command()
async def ping(ctx):
    await ctx.send("I am made of hollow bones")


@bot.command()
async def hello(ctx):
    await ctx.send("I will eat your eyes")


@bot.command()
async def name(ctx):
    response = f"I am Burak and I hate {ctx.message.author.name}"
    await ctx.send(response)


@bot.command()
async def generate_image(ctx):
    await ctx.send('Fuck you')


@bot.command()
async def yarin(ctx):
    file = discord.File(r"C:\Users\USER\Pictures\goblin.png", filename="goblin.png")
    await ctx.send(file=file)


@bot.command()
async def phrase(ctx):
    await ctx.send("Sırtım ağrıyor ve hükümeti suçluyorum")


@bot.command()
async def glorp(ctx):
    await ctx.send("Plip plop plip plop")


@bot.command()
async def bye(ctx):
    await ctx.send("I go eat doner kebab")
    await bot.close()


@bot.command()
async def join(ctx):
    if ctx.author.voice:  # Checks if the user is in a voice channel
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"I come to preach in {channel.name}!")
    else:
        await ctx.send("You offended Burak")


@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("I leave you smell like cow")
    else:
        await ctx.send("Burak not speaking")


@bot.command()
async def speak(ctx):
    if ctx.voice_client:
        voice_client = ctx.voice_client
        if not voice_client.is_playing():
            audio = discord.FFmpegPCMAudio(r"C:\Users\USER\Music\cough.mp3")
            await voice_client.play(audio)
        else:
            await ctx.send("I am already speaking you foul degenerate")
    else:
        await ctx.send("Burak not in voice channel")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked. 👢")
    except discord.Forbidden:
        await ctx.send("I don't have permission to kick this user.")
    except discord.HTTPException:
        await ctx.send("Something went wrong trying to kick the user.")


@bot.command()
async def lovely(ctx):
    image = discord.File(r"C:\Users\USER\Pictures\Saved Pictures\evil.jpg", filename='tutman.jpg')
    await ctx.send(file=image)


@bot.command()
async def play(ctx):
    await ctx.send('Burak will roll the dice')
    chosen = floor(random() * 10)
    await ctx.send(f'number chosen is {chosen}')
    await ctx.send(responses[chosen])

@bot.command()
async def wisdom(ctx):
    for i in range(20):
        await ctx.author.send('Go fuck yourself')

responses = {
    0: 'I kill myself',
    1: 'I will boil your babies',
    2: 'Cute monki',
    3: 'You tell me a shrimp fried this rice?',
    4: 'You just lost your eyebrows privileges',
    5: 'DOWN WITH ARMENIA!',
    6: 'SLAYYYY TURKISH QUEEEN',
    7: 'I have 11 teeth',
    8: '...--- --.-. .--. ..--.. -.- ..- - ..-.',
    9: '<Self Destruct>'
}

bot.run(os.getenv('TOKEN'))
