import discord
import random
import asyncio
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hi! I am a bot, {client.user}!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
    elif message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
            answer = random.randint(1, 10)
            try:
                guess = await client.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')
            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send(f'Oops. It is actually {answer}.')
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001F44B")
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emoji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))   


client.run("MTEyMTc4NDc3Njc0Mzk4OTM1MQ.Gsz_SZ.V0bStBuRGSDbw24Vrp1yK5ISzoMKkcsfukCbNc")