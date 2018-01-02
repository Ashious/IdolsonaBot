from random import choice, randrange
import datetime

with open('idolsona.txt') as school_idols:
    idolsona = school_idols.read().split('\n')
    idolsona.remove(idolsona[-1])
months =  ["January", "February","March", 'April', "May", 'June',
           "July", "August", 'September', "October", 'November', "December"]

def who(remove_self):
    idolsona.remove(remove_self)
    reply = "It's %s!" % choice(idolsona)
    return reply


def what(question: str):
    time = str(datetime.datetime.utcnow()).split()
    if 'date' in question:
        exact_time = time[0].split('-')
        if exact_time[1].startswith('0'):
            exact_time[1] = exact_time[1][1]
        if exact_time[2].startswith('0'):
            exact_time[2] = exact_time[2][1]
        exact_time[1] = months[int(exact_time[1])-1]
        return "Today is {} {}!".format(exact_time[1], exact_time[2])
    elif 'time' in question:
        half = 'am'
        exact_time = time[1].split(':')
        if int(exact_time[0]) > 12:
            exact_time[0] = int(exact_time[0])-12
            half = 'pm'
        elif exact_time[0] == '00':
            exact_time[0] = '12'
        elif exact_time[0] == '12':
            half = 'pm'
        h_m = str(exact_time[0])+'.'+exact_time[1]+' '+half
        return "It is now "+h_m+'.'
    else:
        return 'I do not know the answer to that question.'


def when():
    thirty_one = ["January", "March", "May", "July", "August", "October", "December"]
    thirty = ['April', 'June', 'September', 'November']
    months = thirty_one+thirty
    months.append('February')
    random_month = choice(months)
    if random_month == 'February':
        random_day = randrange(1, 30)
    elif random_month in thirty:
        random_day = randrange(1, 31)
    else:
        random_day = randrange(1, 32)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday.Sunday"]
    past = ['Yesterday', 'Last week.', 'Last year.', 'Last month.']
    future = ['Tomorrow.', 'Next week.', 'Next year.', 'Next month.', 'One day.', 'Later.']
    present = ['Today.', 'Just now.']
    time = ['Never.',  'On %s maybe?' % choice(days), choice(past), choice(future), choice(present),
            '*looks at calender* {} {} maybe?'.format(random_month, random_day)]
    return choice(time)


def where():
    place = ['Up.', 'Down.', 'In front of you.', 'Behind you.', 'On your left.', 'On your right.', 'Above you.',
             'Below you.', 'Inside you.', 'On you.', 'Somewhere.', 'Anywhere.', 'Everywhere.', 'Right here.',
             'Right there.']
    return choice(place)


def why():
    reply = ['idk', 'Because...', 'Unfortunately, I do not how to answer that question.']
    return choice(reply)


def which():
    return 'Say `hey choose help`!'


def how():
    return 'How should I know?'


def default():
    yes_reply = ["Yes.", "As I see it, yes.", "Certainly.", "I think so...", "Most likely?", '~ :heart:', 'Ok.',
                 "*Signs point to yes*", "100% without a doubt.", "Yes!", "Definitely!", ':ok_woman:',
                 'True!', '{} out of 10!'.format(randrange(5, 11)), '*nods*']
    no_reply = ["THAT'S WRONG!!", "My reply is NO.", "No!", ':no_good:', "I doubt it.", 'Let me think about it. No.',
                '*punches you* :right_fist: No.', "False!", '{} out of 10.'.format(randrange(0, 5)), 'No?']
    maybe_reply = ["¯\_(ツ)_/¯", "Maybe?", "I didn't quite hear you, what?", "What?!", "Can you ask later?",
                   "I can't tell you now...", "*shrug* idk", "Can you repeat that?", 'What is that?',
                   'idk :expressionless:', 'Who knows?', "I can't understand you :sweat:", ':thonk:',
                   '┐(´ー｀)┌', "ヽ(´ー`)ノ", "╮(─▽─)╭", ':thinking_face:', 'Oh.', 'lol',
                   'I give it {} out of 10.'.format(randrange(3, 8)), "I don't believe it. :expressionless:"]
    return choice(choice([yes_reply, no_reply, maybe_reply]))
