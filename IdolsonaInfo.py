def birthday():
    birthday_list = {'Saki': 'Jan 18',
                     'Kayo': 'Jan 24',
                     'Salamander': 'Jan 28',
                     'Maya': 'Jan 30',
                     'Meow': 'Feb 9',
                     'Kyle': 'Feb 13',
                     'Mahiru': 'Feb 16',
                     'Koko': 'Feb 17',
                     'Ciel': 'Feb 17',
                     'Alyse': 'Feb 19',
                     'Neo': 'Feb 22',
                     'Risa': 'Mar 13',
                     'Ikku': 'Mar 20',
                     'Rubae': 'Mar 29',
                     'Reika': 'Apr 1',
                     'Kurumi': 'Apr 10',
                     'Asuka': 'Apr 16',
                     'Kyo': 'May 1',
                     'Chisa': 'May 9',
                     'Hayato': 'May 13',
                     'Elizabeth': 'May 18',
                     'Yuzuru': 'Jun 4',
                     'Hoshi': 'Jun 6',
                     'Nika': 'Jun 9',
                     'Seika': 'Jun 21',
                     'Meri': 'Jul 30',
                     'Masumi': 'Aug 2',
                     'Masu': 'Aug 2',
                     'Niko': 'Aug 5',
                     'Cat': 'Aug 11',
                     'Nami': 'Aug 12',
                     'Wilcza': 'Aug 13',
                     'Zach': 'Aug 22',
                     'Cin': 'Aug 23',
                     'Yolo': 'Sep 5',
                     'Thug': 'Sep 16',
                     'Miki': 'Sep 19',
                     'Yuu': 'Sep 19',
                     'Draq': 'Sep 21',
                     'Tea': 'Sep 21',
                     'Alex': 'Sep 22',
                     'Hannah': 'Sep 24',
                     'Andrea': 'Sep 26',
                     'Kohaku': 'Oct 3',
                     'Myra': 'Oct 7',
                     'Justin': 'Oct 16',
                     'Shiori': 'Oct 20',
                     'Chiharu': 'Oct 29',
                     'Misaki': 'Oct 31',
                     'Hotaru': 'Nov 22',
                     'Roro': 'Nov 25',
                     'Anne': 'Dec 9',
                     'Haru': 'Dec 11',
                     'Bob': 'Dec 11',
                     'Yui': 'Dec 18',
                     'Ffion': 'Dec 19',
                     'Aurora': 'Dec 23',
                     'Passionate': 'Dec 24',
                     'Luka': 'Dec 25'
                     }
    return birthday_list


def owners():
    owner_list = {'229230267842297856': ['Justin', 'Seika'],
                  '282679665024303104': ['Zach'],
                  '236167289269911552': ['Bob'],
                  '235744545378140160': ['Chisa', 'Masumi'],
                  '235455115883053056': ['Aurora'],
                  '282025498861633536': ['Hoshi', 'Hayato', 'Reika', 'Mahiru', 'Haru', 'Yuu', 'Kurumi', 'Miki'],
                  '281899537482907648': ['Alex', 'Elizabeth'],
                  '224947766118318080': ['Luka'],
                  '174804016692330496': ['Ikku', 'Yuzuru', 'Chiharu'],
                  '146407831849926656': ['Misaki'],
                  '279012729090736129': ['Miki'],
                  '277330160553033728': ['Neo', 'Shiori'],
                  '321747275535613963': ['Chiyoko', 'Maya', 'Hotaru', 'Kyo', 'Kohaku', 'Asuka', 'Nami', 'Risa', 'Yui'],
                  'default': ['']
                  }
    return owner_list


def idol_help(command: str):
    header = "```{} command:```".format(command.title())
    if command == 'flip':
        guide = "*Flips a table at someone.*\n" + \
                "**Usage: hey {idolsona(optional)} flip {name(optional)}**\n" + \
                "#This is an independent command, a random idolsona will be chosen if " + \
                "no available idolsonas is specified."
        return header+guide
    elif command == 'throw':
        guide = "*Throws something at someone.*\n" + \
                "**Usage: hey {idolsona(optional)} flip {name(optional)}**\n" + \
                "#This is an independent command, a random idolsona will be " + \
                "chosen if no available idolsonas is specified."
        return header+guide
    elif command == 'pat':
        guide = "*Give out pats.* \n" + \
                "**Usage: hey {idolsona(optional)} pat {name | mention}**\n" + \
                "#This is an independent command, a random idolsona will be chosen if " + \
                "no available idolsonas is specified."
        return header+guide
    elif command == 'shrug':
        guide = "*Shrug idk*\n" + \
                "**Usage: hey {idolsona(optional)} shrug**\n" + \
                "#This is an independent command, a random idolsona will be chosen if " + \
                "no available idolsonas is specified."
        return header+guide
    elif command == 'art':
        guide = "*Shows you something beautiful.*\n" + \
                "**Usage: hey art {mention(optional)}**\n" + \
                "#If no user is mentioned, defaults to caller instead.\n" + \
                "#This is an image command, no idolsona needs to be specified."
        return header+guide
    elif command == 'cinnamon':
        guide = "*For those who are too precious for this world.*\n" + \
                "**Usage: hey cinnamon {mention(optional)}**\n" + \
                "#If no user is mentioned, defaults to caller instead. Also works with a sent image or image url\n" + \
                "#This is an image command, no idolsona needs to be specified."
        return header+guide
    elif command == 'idolsonascout':
        guide = "*Idolsona scouting simulator based on SIF.*\n" + \
                "**Usage: hey idolsonascout { | 11 | bt | bt2 | bt3 }**"
        return header+guide
    elif command == 'remember':
        guide = "*Idolsona tagging system. Each tags are different for each idolsona.*\n" + \
                "**Usage: \nhey {idolsona} remember {tag name}**\n***Idolsona:*** **What shall I remember?**\n" + \
                "**{Enter tag content}**\n" + \
                "#To delete tag, see `help forget`."
        return header+guide
    elif command == 'forget':
        guide = "*Deletes an idolsona tag.*\n" + \
                "**Usage: hey {idolsona} forget {tag name}**\n" + \
                "#Only tag author can delete the tag."
        return header+guide
    elif command == 'meme':
        guide = "*Makes a meme.*\n" + \
                "**Usage: hey meme {mention(optional)} {upper text},{lower text}**\n" + \
                "#If no user is mentioned, defaults to caller instead.\n" + \
                "#This is an independent command, no idolsona needs to be specified."
        return header+guide
    elif command == 'repeat':
        guide = "*Makes an idolsona repeat what you said.*\n" + \
                "**Usage: hey {idolsona(optional)} repeat {what you want the idolsona to say}**\n" + \
                "#This is an independent command, a random idolsona will be chosen if " + \
                "no available idolsonas is specified."
        return header+guide
    elif command == 'rate':
        guide = "*Show you something beautiful.*\n" + \
                "**Usage: hey {idolsona(optional)} rate {something/someone}**\n" + \
                "#If no user is mentioned, defaults to caller instead."
        return header+guide
    elif command == 'ask':
        guide = "*Ask an idolsona a question. ~~Doesn't guarantee an exact answer though :P~~*\n" + \
                "**Usage: hey {idolsona(optional)} {question}?**\n" + \
                "#This is an independent command, a random idolsona will be chosen if " + \
                "no available idolsonas is specified.\n#Will not be called if question is not ended with '?'"
        return header+guide
    elif command == 'hug':
        guide = "*Gives out hugs.*\n" + \
                "**Usage: hey hug { me | name | mention(optional)}**\n" + \
                "#This is an independent command, a random idolsona will be chosen if " + \
                "no available idolsonas is specified."
        return header+guide
    elif command == 'choose':
        guide = "*Have an idolsona make important life decisions for you.*\n" + \
                "**Usage: hey {idolsona(optional)} choose option1,option2,...**\n" + \
                "#This is an independent command, a random idolsona will be chosen if " + \
                "no available idolsonas is specified.\n" + "#OPTIONS MUST BE SEPARATED BY COMMAS"
        return header+guide
    else:
        with open('idolsona.txt') as idols:
            idolsona_list = idols.read().split('\n')
        idolsona_list.remove(idolsona_list[-1])
        idolsona_list.sort()
        all_members = ", ".join(idolsona_list)
        return "Current prefix: 'hey '\n" +\
               "```Independent commands: (idolsona name doesn't have to be specified)```" +\
               "ask, repeat, pat, hug, choose, flip, throw, shrug, art, cinnamon, meme, idolsonascout, help\n" +\
               "```Idolsona dependent commands: (idolsona name needed to be specified)```" +\
               "remember, forget, ask\n" +\
               "```Other trigger words:``` *secret for reasons*\n" +\
               "```Available idolsonas:```" + all_members+"\n\n`Type 'hey help {command name} for more info.'`"
