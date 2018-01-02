import discord
from random import choice, randrange, shuffle
import asyncio
import logging
from ProjectIdolsona import IdolsonaImages, IdolsonaTags, IdolsonaInfo, IdolsonaScout, IdolsonaAsk
import emoji
from pathlib import Path
import pickle
import time

logging.basicConfig(level=logging.INFO)
client = discord.Client(max_messages=10000)
file = discord.File
image_file = 'Images\\'
with open('idolsona.txt') as names:
    idolsona_list = names.read().split('\n')
    idolsona_list.remove(idolsona_list[-1])
emotion = [':flushed:', ':kissing_closed_eyes:', "( ͡° ͜ʖ ͡°)>⌐■-■ ( ͡⌐■ ͜ʖ ͡-■)", ':worried:', '(˶◕‿◕˶✿)',
           " ( ͡~ ͜ʖ ͡°)", ":innocent:", ':wink:', ':smiling_imp:', ':grinning:', ':grin:', '(⁄ ⁄◕⁄ω⁄◕⁄ ⁄✿)',
           ':smile:', ':smiley:', 'Thanks for the info.', ':sunglasses:', ':rage:', ':angry:', '(⁄ ⁄◕⁄‿⁄◕⁄ ⁄✿)',
           ':rolling_eyes:', ':cry:', ':sleepy:', ':cold_sweat:', ':frowning2:', ':frowning:', 'Oh.', 'Upupupu~',
           '(◕◡◕✿)', '(◕д◕✿)!', 'ಠ_ಠ', 'ರ_ರ']
owner_list = IdolsonaInfo.owners()
birthday_list = IdolsonaInfo.birthday()


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

        for ind in birthday_list.keys():
            if birthday_list[ind] == date_today:
                birthday.append(ind)
                special_day = True

        if special_day and round_hour == 12 and not change_once:
            happy_birthday = ", ".join(birthday)
            greeter = choice(idolsona_list)
            while greeter in birthday:
                greeter = choice(idolsona_list)
            await channel.edit(topic='🎊🎉 Happy Birthday {} ({})! 🎉🎊'.format(happy_birthday, date_today))
            await channel.send('**{}:** Happy birthday {}!🎉'.format(greeter, happy_birthday))
            change_once = True
        elif not special_day:
            if 'Happy Birthday' in channel.topic:
                await channel.edit(topic=' ')
            else:
                await channel.edit(topic=channel.topic)

        print('----------------------------------------')
        print(date_today)
        print(time_now)
        print('Next timecheck in {} minutes {} seconds'.format(str(m_timecheck), str(s_timecheck)))
        print('----------------------------------------')
        print('From discord:')
        await asyncio.sleep(s_timecheck + m_timecheck * 60)


async def commands(command: str, message: discord.Message, idol: str, is_random=True):
    club_members = message.guild.members
    chance = randrange(1, 1001)
    channel = message.channel
    await channel.trigger_typing()
    each_content = emoji.demojize(message.content).lower().split()
    face = ["(╯°□°）╯︵", "(ノಠ益ಠ)ノ彡", "(ノ￣皿￣）ノ ︵", "(╯ರ ~ ರ）╯︵", "(ﾉ≧∇≦)ﾉ ﾐ"]
    dialogue = '**%s:** ' % idol
    trigger = each_content[1:]
    if idol.lower() in trigger[:3]:
        trigger.remove(idol.lower())
    if command in trigger[:3]:
        trigger.remove(command)
    target = " ".join(trigger)
    if command == 'help':
        trigger.append('')
        reply = IdolsonaInfo.idol_help(trigger[0])
        await channel.send(reply)
    elif command == 'flip' or command == 'throw':
        if command == 'flip':
            item = ['┻━┻']
        else:
            item = [':doughnut:', ':anchor:', ':bomb:', ':urn:', ':crystal_ball:', ':hammer:', ':pick:',
                    ':sweat_drops:']

            if 'me' in trigger:
                trigger[trigger.index('me')] = message.author.name
            if 'you' in target:
                await channel.send(
                    dialogue + "You think that's funny? How about this?! " + choice(face) + choice(item) +
                    message.author.mention)
                return
            if 'at' in trigger and len(trigger) >= 2:
                item = trigger[:trigger.index('at')]
                if message.author.name in item:
                    item = [message.author.name]
                if trigger[-1] == 'at':
                    target = choice(club_members)
                else:
                    target = trigger[-1]
            elif len(trigger) >= 2:
                target = trigger[-1]
                item = trigger[:trigger.index(target)]
                if message.author.name in item:
                    item = [message.author.name]
            elif len(trigger) > 1:
                target = trigger[-1]
                trigger.remove(target)
                item = trigger
            elif len(trigger) > 0:
                item = trigger
                target = choice(club_members).name
            else:
                item = [':doughnut:', ':anchor:', ':bomb:', ':urn:', ':crystal_ball:', ':hammer:', ':pick:',
                        ':sweat_drops:']
                target = choice(club_members).name

        if idol.lower() in target or client.user in message.mentions:
            await channel.send(dialogue+"You think that's funny? How about this?! " + choice(face) + choice(item) +
                               message.author.mention)
        else:
            reactor = target.title()
            if message.author.name in item:
                reactor = message.author.name
            if reactor.startswith('<') and reactor.endswith('>') and '@' in reactor:
                reactor_id = ''
                ignore = ['<', '>', '@']
                for num in reactor:
                    if num in ignore:
                        pass
                    else:
                        reactor_id = reactor_id+num
                member = message.guild.get_member(int(reactor_id))
                reactor = member.name
            if chance <= 200:
                nice_or_not = "┬─┬ノ( º _ ºノ) No, let's not."
            else:
                react = ['Ow!', 'That hurts!', 'Uwaa!', ':scream:', '*dodges like a boss*', ':scream:', ':imp:',
                         ':cry:']
                nice_or_not = "Take this {}! {}{}\n**{}:** {}".format(target.title(), choice(face), choice(item),
                                                                      reactor, choice(react))
            await channel.send(dialogue+nice_or_not)
    elif command == 'pat':
        if len(trigger) != 0 and 'me' not in trigger:
            for t in trigger:
                if t.title() in idolsona_list:
                    trigger[trigger.index(t)] = t.title()
            teddy = " ".join(trigger)
        else:
            teddy = 'you'
        all_gif = open('C:\\Users\\Hp\\PycharmProjects\\ProjectIdolsona\\Images' +
                       '\\pat\\pat{}.gif'.format(randrange(1, 26)), 'rb')
        pat_gif = file(all_gif)
        await channel.send(dialogue + '*pats {}* There there~'.format(teddy), file=pat_gif)
    elif command == 'shrug':
        shrug = ['¯\\\_(ツ)_/¯', '┐(°‿°)┌', '¯\\\_(°‿°)_/¯', '¯\\\_(˶′◡‵˶)_/¯', 'ʅ（´◔౪◔）ʃ',
                 '¯\\\_(´・ω・｀)_/¯', '¯\\\_(⌣̯̀ ⌣́)_/¯', '┐(￣ー￣)┌', 'ʅ(°﹃°)ʃ', '͡¯\\\_(°_o)_/¯']
        await channel.send(dialogue+choice(shrug))
    elif command == 'art':
        await channel.send(file=IdolsonaImages.beautiful(message))
    elif command == 'cinnamon':
        await channel.send(file=IdolsonaImages.cinnamon(message))
    elif command == 'idolsonascout':
        await asyncio.sleep(5)
        await channel.send(IdolsonaScout.scout(message))
    elif command == 'hug':
        if len(trigger) != 0 and 'me' not in trigger:
            for t in trigger:
                if t.title() in idolsona_list:
                    trigger[trigger.index(t)] = t.title()
            teddy = " ".join(trigger)
        else:
            teddy = 'you'
        hug = ['Hagu!', 'Gyu~', 'There there~']
        hugmoji = ["(っ˘▽˘̩)っ", "(っ´▽｀)っ", "╰(*´︶`*)╯", "(つ≧▽≦)つ", "(づ￣ ³￣)づ", "⊂(´・ω・｀⊂)",
                   '(つˆ⌣ˆ)つ', '～～(つˆДˆ)つ', 'ヽ(＾Д＾)ﾉ']
        all_gif = open('C:\\Users\\Hp\\PycharmProjects\\ProjectIdolsona\\Images' +
                       '\\hug\\hug{}.gif'.format(randrange(1, 32)), 'rb')
        hug_gif = file(all_gif)
        await channel.send('{}*hugs {}* {} {}'.format(dialogue, teddy, choice(hug), choice(hugmoji)), file=hug_gif)
    elif len(each_content) <= 2:
        await channel.send('**{}:** {}'.format(idol, choice(emotion)))
    elif (command == 'remember' or command == 'forget' or command == 'tag') and not is_random and len(trigger) != 0:
        blacklist = ['remember', 'forget', 'author', 'tag']
        if command == 'remember':
            if trigger[0] in blacklist or 'author' in trigger:
                await channel.send(dialogue+"That tag name is not available!")
            elif len(trigger) > 10:
                await channel.send(dialogue+"Too long!")
            else:
                def req(m: discord.Message):
                    return message.channel == m.channel and message.author == m.author

                await message.channel.send("**%s:** What shall I remember?" % idol)
                try:
                    contents = await client.wait_for('message', check=req, timeout=90)
                except asyncio.TimeoutError:
                    await channel.send('**%s:** Never mind then.' % idol)
                else:
                    is_exist = IdolsonaTags.check_for_tag(idol, "_".join(trigger), message.author)
                    if is_exist:
                        reply = await IdolsonaTags.tag_edit(idol, "_".join(trigger), message.author,
                                                            emoji.demojize(contents.content), contents.attachments)
                        await channel.send(dialogue + reply)
                    else:
                        reply = await IdolsonaTags.tag_create(idol, "_".join(trigger), emoji.demojize(contents.content),
                                                              message.author, contents.attachments)
                        await channel.send(dialogue + reply)
        elif command == 'forget':
            await channel.send(dialogue + IdolsonaTags.tag_delete(idol, "_".join(trigger), message.author))
        elif command == 'tag':
            if trigger[0] == 'list':
                await channel.send(IdolsonaTags.get_tag_list(idol, message.author))
            elif 'author' in trigger:
                trigger.remove('author')
                await channel.send(dialogue+IdolsonaTags.get_author(idol, "_".join(trigger), message.author))
            else:
                await channel.send("See `hey help tag` for usage.")
    elif command == 'meme':
        if len(message.mentions) == 0:
            avatar = message.author
        else:
            avatar = message.mentions[0]
        await channel.send(file=IdolsonaImages.meme(avatar, target))
    elif command == 'repeat':
        sentence = target.capitalize()
        if sentence[-1].isalnum():
            sentence = sentence + '!'
        await channel.send("**{}:** {}".format(idol, sentence))
    elif command == 'rate':
        await channel.send("**{}:** {} out of 100!".format(idol, randrange(0, 101)))
    elif command == 'choose':
        options = " ".join(trigger).split(',')
        await channel.send(dialogue + 'I choose %s' % choice(options))
    elif not is_random:
        tag_name = ''
        tag_call = False
        if not IdolsonaTags.check_for_tag(idol, 'a name tag that no one will use', message.author):
            with open(r'C:\Users\Hp\PycharmProjects\ProjectIdolsona\bot' + '\\{}\\tag_list.txt'.format(idol),
                      encoding='utf-8') as tag_list:
                all_tags = tag_list.read().split('\n')
            all_tags.remove('')
            for t in all_tags:
                if '_' in t:
                    all_tags[all_tags.index(t)] = " ".join(t.split('_'))
            shuffle(all_tags)
            for tag in all_tags:
                if tag in target:
                    tag_name = "_".join(tag.split())
                    tag_call = True
                    break
        if len(trigger) == 0:
            await channel.send(dialogue + choice([choice(emotion), IdolsonaAsk.default()]))
        elif tag_call:
            await channel.send(dialogue + IdolsonaTags.get_tag(idol, tag_name, message.author))
        elif trigger[0] == 'who':
            await channel.send(dialogue + IdolsonaAsk.who(idol))
        elif trigger[0] == 'what':
            await channel.send(dialogue + IdolsonaAsk.what(target))
        elif trigger[0] == 'when':
            await channel.send(dialogue + IdolsonaAsk.when())
        elif trigger[0] == 'where':
            await channel.send(dialogue + IdolsonaAsk.where())
        elif trigger[0] == 'why':
            await channel.send(dialogue + IdolsonaAsk.why())
        elif trigger[0] == 'which':
            trigger.remove('which')
            await channel.send(dialogue + IdolsonaAsk.which())
        elif trigger[0] == 'how':
            await channel.send(dialogue + IdolsonaAsk.how())
        else:
            await channel.send(dialogue + choice([choice(emotion), IdolsonaAsk.default()]))


@client.async_event
async def on_message(message: discord.Message):
    channel = message.channel
    lower_text = emoji.demojize(message.content).lower()
    content = lower_text.split()
    chance = randrange(1, 1001)

    hello = ['Hello!', 'Hi~', 'Good morning~', 'Hi!', 'Hello~', 'Heyo!', 'Hewo!', 'Bonjour!']
    bye = ['Bye!', 'Goodbye~', 'Sayonara~', 'Byebye~', ':wave:', 'See you!', 'Laters!']

    idol = choice(idolsona_list)
    is_random = True
    who_is_first = 5
    for student in idolsona_list:
        if student.lower() in content[:4] and content.index(student.lower()) < who_is_first:
            who_is_first = content.index(student.lower())
            idol = student
            is_random = False
    channel_blacklist = [313815181497073666, 327121787139784705, 319007389108011008, 376648225521664000]
    category_blacklist = [362212530854035467, 388275575371988992]
    if channel == message.author.dm_channel and content[0] == 'hey' and len(content) > 3:
        print('DM CHANNEL:')
        print('{}: {}'.format(message.author.name, message.content))
        each_content = emoji.demojize(message.content).lower().split()
        dialogue = '**%s:** ' % idol
        trigger = each_content[1:]
        if idol.lower() == trigger[0]:
            trigger.remove(idol.lower())
        command = trigger[0]
        if command == trigger[0]:
            trigger.remove(command)
        blacklist = ['remember', 'forget', 'tag']
        if command == 'remember':
            if trigger[0] in blacklist or 'author' in trigger:
                await channel.send(dialogue + "That tag name is not available!")
            elif len(trigger) > 10:
                await channel.send(dialogue + "Too long!")
            else:
                def req(m: discord.Message):
                    return message.channel == m.channel and message.author == m.author

                await message.channel.send("**%s:** What shall I remember?" % idol)
                try:
                    contents = await client.wait_for('message', check=req, timeout=90)
                except asyncio.TimeoutError:
                    await channel.send('**%s:** Never mind then.' % idol)
                else:
                    is_exist = IdolsonaTags.check_for_tag(idol, "_".join(trigger), message.author)
                    if is_exist:
                        reply = await IdolsonaTags.tag_edit(idol, "_".join(trigger), message.author,
                                                            emoji.demojize(contents.content), contents.attachments)
                        await channel.send(dialogue + reply)
                    else:
                        reply = await IdolsonaTags.tag_create(idol, "_".join(trigger), emoji.demojize(contents.content),
                                                              message.author, contents.attachments)
                        await channel.send(dialogue + reply)
        elif command == 'forget':
            await channel.send(dialogue + IdolsonaTags.tag_delete(idol, "_".join(trigger), message.author))
        elif command == 'tag':
            if trigger[0] == 'list':
                await channel.send(IdolsonaTags.get_tag_list(idol, message.author))
            elif 'author' in trigger:
                trigger.remove('author')
                await channel.send(dialogue+IdolsonaTags.get_author(idol, "_".join(trigger), message.author))
    elif channel == message.author.dm_channel:
        print('{}: {}'.format(message.author.name, message.content))
        await channel.send('**Available commands: remember, forget, tag**')
    elif message.author.bot or len(content) < 1 or lower_text == 'hey' or channel.id in\
            channel_blacklist or channel.category_id in category_blacklist:
        return
    else:
        print('In ' + message.guild.name + ',' + channel.name + ':')
        print('   ' + message.author.name + ':' + message.clean_content)
        if "u's" in content:
            f = open(image_file + 'trigger\\dia.png', 'rb')
            ff = file(f)
            await channel.trigger_typing()
            await asyncio.sleep(3)
            lecture = "Can it be, that you're talking about μ's? How dare you mistaken their name?! Hm? " + \
                      "In the school idol world, μ's are legendary. " + \
                      "They're the holy ground, holy scripture, " + \
                      "the origin of life equivalent to the universe. " + \
                      "And you mistaken their name?! Absolutely ridiculous."
            await channel.send(lecture, file=ff)
        if 'aquors' in content:
            await channel.send('***AQOURS***')
        if 'pizza' in lower_text and chance <= 500:
            await channel.send('**Justin:** Did someone said pizza? :eyes:')
            await asyncio.sleep(3)
            await message.add_reaction('🍕')
        if 'despair' in lower_text and chance <= 500:
            despair = ["AH SWEET DESPAIR", 'Upupupupu~', 'DESPAIR!']
            with open(image_file + 'trigger\\junko{}.png'.format(randrange(1, 3)), 'rb') as junko:
                upu = file(junko)
                await channel.send('**Luka:** {}'.format(choice(despair)), file=upu)
        if 'suicid' in lower_text:
            no_suicide = [":sad:", "Suicide is bad."]
            await channel.send("**{}:** {}".format(idol, choice(no_suicide)))
        if 'donut' in lower_text and chance <= 666:
            await channel.send('**Hoshi:** DONUTS!!!')
            await asyncio.sleep(3)
            await message.add_reaction('🍩')
        if 'mint' in content:
            await channel.send('**Asuka:** I heard mint :eyes:')
        if 'prank' in content:
            await channel.send('**Nami:** Prank you say? :eyes:')
        if 'go' in lower_text and 'study' in lower_text and chance <= 800:
            reply = '**{}:** {}'.format(idol, choice(['**GO STUDY**', 'Study well~']))
            await asyncio.sleep(5)
            await channel.send(reply)
        elif 'go' in lower_text and 'sleep' in lower_text and chance <= 200:
            reply = choice(['***GO TO SLEEP***', 'Good night~'])
            await channel.send("**{}:** {}".format(idol, reply))
        if ('hello' in lower_text or 'hi' in content) and chance <= 750:
            reply = choice(hello)
            await channel.send('**{}:** {}'.format(idol, reply))
        if 'bye' in lower_text and chance <= 500:
            reply = choice(bye)
            await channel.send('**{}:** {}'.format(idol, reply))
        if 'tfw' in content:
            tfw = ['tfw.png', 'tfw2.jpg']
            f = open(image_file + 'tfw\\' + choice(tfw), 'rb')
            ff = file(f)
            await channel.send(file=ff)
        if 'rip' in content and chance <= 500:
            await asyncio.sleep(5)
            await channel.send('**{}: R.I.P**'.format(idol))
        if 'shut' in content and 'up' in content and chance <= 800:
            h = open(image_file + 'trigger\\NozoHeh.png', 'rb')
            hh = file(h)
            await channel.send(file=hh)
        if content[0] == 'im' and chance <= 200 and 1 < len(content) <= 3:
            joke = " ".join(content[content.index('im') + 1:])
            if chance <= 111:
                reply = "Hello {} I'm {}".format(joke, idol)
            elif chance > 222:
                reply = 'You are safe for now {} :eyes:'.format(joke)
            else:
                reply = 'You are safe for now {} :eyes:'.format(message.author.name)
            await channel.trigger_typing()
            await asyncio.sleep(7)
            await channel.send("**{}:** {}".format(idol, reply))
        furry = ['owo', '0w0', '0wo', 'ow0', 'nya', 'uwu']
        for owo in furry:
            if owo in lower_text and chance <= 200:
                fur = ['...Furry', "OwO what's this?", 'Furry detected', '**OwO**', 'Nya']
                await channel.send('**{}:** {}'.format(idol, choice(fur)))
                break
            elif owo in lower_text and chance <= 100:
                await channel.trigger_typing()
                await channel.send("**{}:** *breathes in*".format(idol))
                await asyncio.sleep(7)
                await channel.send("**{}:** Furry.".format(idol))
                break
        if (content[0] == 'hey' or message.content.startswith('<@%s>' % client.user.id)) and not \
                is_random and len(content) > 2:
            trigger_message = content[content.index(idol.lower())+1]
            content.remove('hey')
            if idol.lower() in content:
                content.remove(idol.lower())
            tag = "_".join(content)
            if lower_text.endswith('?'):
                trigger_message = 'question'
            if IdolsonaTags.check_for_tag(idol, tag, message.author):
                tag_images = []
                for i in range(1, 11):
                    check_image = 'C:\\Users\\Hp\\PycharmProjects\\ProjectIdolsona\\' + \
                                  'bot\\{}\\tags\\{}.png'.format(idol, tag + str(i))
                    my_file = Path(check_image)
                    if my_file.is_file():
                        image = open(check_image, 'rb')
                        tag_images.append(file(image))
                    else:
                        break
                if len(tag_images) == 0:
                    await channel.send('**{}:** {}'.format(idol, IdolsonaTags.get_tag(idol, tag, message.author)))
                elif len(tag_images) == 1:
                    await channel.send('**{}:** {}'.format(idol, IdolsonaTags.get_tag(idol, tag, message.author)),
                                       file=tag_images[0])
                else:
                    await channel.send('**{}:** {}'.format(idol, IdolsonaTags.get_tag(idol, tag, message.author)),
                                       files=tag_images)
                for i in range(1, 11):
                    check_image = 'C:\\Users\\Hp\\PycharmProjects\\ProjectIdolsona\\' + \
                                  'bot\\{}\\tags\\{}.png'.format(idol, tag + str(i))
                    my_file = Path(check_image)
                    if my_file.is_file():
                        image = open(check_image, 'rb')
                        image.close()
                    else:
                        break
            else:
                await commands(trigger_message, message, idol, False)
        elif content[0] == 'hey' or message.content.startswith('<@%s>' % client.user.id):
            trigger_message = content[1]
            await commands(trigger_message, message, idol)
        if 'idolsonascout' not in lower_text:
            stats = IdolsonaScout.user_stats(message.author)
            gem = stats['gems']
            if chance == 1000:
                gem += 50
            elif chance <= 50:
                gem += 2
            elif chance <= 500:
                gem += 1
            stats['gems'] = gem
            with open("C:\\Users\\Hp\\PycharmProjects\\ProjectIdolsona\\Scouting\\" +
                      str(message.author.id) + '\\stats.txt', 'w+') as update, \
                    open("C:\\Users\\Hp\\PycharmProjects\\ProjectIdolsona\\Scouting\\" +
                         str(message.author.id) + '\\raw_stats.txt', 'wb+') as raw_update:
                update.write(str(stats))
                pickle.dump(stats, raw_update)
        if not is_random:
            rp = discord.Game(name='as ' + idol)
        else:
            name = choice(['as ' + idol, 'hey help'])
            rp = discord.Game(name=name)
        await client.change_presence(game=rp, status=discord.Status.online)


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


@client.async_event
async def on_member_join(member: discord.Member):
    channel = client.get_channel(313815059967246339)
    await channel.send('**{}:** Welcome, {}!'.format(choice(idolsona_list), member.mention))


@client.async_event
async def on_member_remove(member):
    channel = client.get_channel(313815059967246339)
    await channel.send("**{}:** Goodbye, {}...".format(choice(idolsona_list), member.name))

client.run(process.env.BOT_TOKEN)
