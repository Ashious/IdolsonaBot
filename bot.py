import discord
import emoji

client = discord.Client(max_messages=10000)


@client.async_event
async def on_message(message: discord.Message):
    channel = message.channel
    lower_text = message.content.lower()
    content = lower_text.split()
    if channel == message.author.dm_channel:
        await channel.send('**Available commands: remember, forget, tag**')
    elif message.author.bot or len(content) < 1 or lower_text == 'hey':
        return
    else:
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
