import discord
import asyncio
import logging
import time
import emoji

logging.basicConfig(level=logging.INFO)
client = discord.Client(max_messages=10000)


@client.async_event
async def on_connect():
    await asyncio.sleep(5)
    while not client.is_closed():
        await asyncio.sleep(1)
        print('----------------------------------------')
        clock = time.asctime(time.localtime(time.time())).split()
        time_now = clock[3]
        hms_now = time_now.split(':')
        next_m_update = 59 - int(hms_now[1])
        next_s_update = 60 - int(hms_now[2])
        print('Next update in {} minutes {} seconds'.format(str(next_m_update), str(next_s_update)))
        print('----------------------------------------')
        print('From discord:')
        await asyncio.sleep(next_s_update + next_m_update * 60)


@client.async_event
async def on_ready():
    print('----------------------------------------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    change_once = False
    while not client.is_closed():
        name = choice(['as ' + choice(idolsona_list), 'hey help'])
        rp = discord.Game(name=name)
        await client.change_presence(game=rp, status=discord.Status.online)
        await asyncio.sleep(1)
        channel = client.get_channel(313815059967246339)
        birthday = []
        special_day = False
        clock = time.asctime(time.localtime(time.time())).split()
        date_today = '{} {}'.format(clock[1], clock[2])
        time_now = clock[3]
        hms = time_now.split(':')
        round_hour = int(hms[0])
        m_timecheck = 59 - int(hms[1])
        s_timecheck = 60 - int(hms[2])

        print('----------------------------------------')
        print(date_today)
        print(time_now)
        print('Next timecheck in {} minutes {} seconds'.format(str(m_timecheck), str(s_timecheck)))
        print('----------------------------------------')
        print('From discord:')
        await asyncio.sleep(s_timecheck + m_timecheck * 60)


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
    print(user.name)
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

client.run(process.env.BOT_TOKEN)
