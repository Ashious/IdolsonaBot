import discord
import asyncio
import logging
import time
import emoji

logging.basicConfig(level=logging.INFO)
client = discord.Client(max_messages=10000)


@client.async_event
async def on_message(message: discord.Message):
    channel = message.channel
    lower_text = emoji.demojize(message.content).lower()
    content = lower_text.split()
    if channel == message.author.dm_channel:
        print('{}: {}'.format(message.author.name, message.content))
        await channel.send('**Available commands: remember, forget, tag**')
    elif message.author.bot or len(content) < 1 or lower_text == 'hey':
        return
    else:
        print('In ' + message.guild.name + ',' + channel.name + ':')
        print('   ' + message.author.name + ':' + message.clean_content)
        if content[0] == 'hey':
            await channel.send("Hello!")


@client.async_event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '\N{THUMBS UP SIGN}':
        if reaction.message.reactions.count('\N{THUMBS UP SIGN}') < 1:
            await reaction.message.add_reaction('👌')
            await asyncio.sleep(0.3)
            await reaction.message.add_reaction('🇳')
            await asyncio.sleep(0.3)
            await reaction.message.add_reaction('🇮')
            await asyncio.sleep(0.3)
            await reaction.message.add_reaction('🇨')
            await asyncio.sleep(0.3)
            await reaction.message.add_reaction('🇪')

client.run(BOT_TOKEN)
