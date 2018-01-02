from random import choice, shuffle, randrange

with open('idolsona.txt') as students:
    idolsona = students.read().split('\n')
    idolsona.remove(idolsona[-1])


def scout(message):
    if '11' in message.content or '10+1' in message.content:
        cards = 0
        scout_result = []
        while cards < 11:
            if cards == 10:
                range_size = 201
            else:
                range_size = 1001
            denominator = randrange(1, range_size)
            idol = choice(idolsona)
            if denominator <= 10:
                rarity = 'UR'
            elif denominator <= 50:
                rarity = 'SSR'
            elif denominator <= 200:
                rarity = 'SR'
            else:
                rarity = 'R'
            card = '**{} {}**'.format(rarity, idol)
            scout_result.append(card)
            cards += 1
        shuffle(scout_result)
        ten = []
        for i in range(0, 10):
            ten.append(scout_result[i])
        first_ten = ', '.join(ten)
        return 'You got: {} and {}!'.format(first_ten, scout_result[10])
    elif 'bt3' in message.content.lower():
        idol = choice(idolsona)
        rarity = 'UR'
        card = '**{} {}**'.format(rarity, idol)
        return 'You got: {}!'.format(card)
    elif 'bt2' in message.content.lower():
        denominator = randrange(1, 1001)
        idol = choice(idolsona)
        if denominator <= 200:
            rarity = 'UR'
        else:
            rarity = 'SSR'
        card = '**{} {}**'.format(rarity, idol)
        return 'You got: {}!'.format(card)
    elif 'bt' in message.content.lower():
        denominator = randrange(1, 1001)
        idol = choice(idolsona)
        if denominator <= 200:
            rarity = 'UR'
        else:
            rarity = 'SR'
        card = '**{} {}**'.format(rarity, idol)
        return 'You got: {}!'.format(card)
    else:
        denominator = randrange(1, 1001)
        idol = choice(idolsona)
        if denominator <= 10:
            rarity = 'UR'
        elif denominator <= 50:
            rarity = 'SSR'
        elif denominator <= 200:
            rarity = 'SR'
        else:
            rarity = 'R'
        card = '**{} {}**'.format(rarity, idol)
        return 'You got: {}!'.format(card)
