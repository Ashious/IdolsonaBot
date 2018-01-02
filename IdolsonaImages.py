import discord
import requests
import re
from PIL import Image, ImageDraw, ImageFont

directory = 'C:\\Users\\Hp\\PycharmProjects\\ProjectIdolsona\\Images\\'
file = discord.File


def beautiful(message: discord.Message):
    #    size1 = 367, 40, 494, 182
    #    size2 = 367, 325, 494, 467
    if len(message.attachments) != 0:
        message.attachments[0].save(directory+'model.png')
    elif len(message.mentions) != 0:
        im = requests.get(message.mentions[0].avatar_url).content
        with open(directory+'model.png', 'wb') as image:
            image.write(im)
    else:
        im = requests.get(message.author.avatar_url).content
        with open(directory+'model.png', 'wb') as image:
            image.write(im)
    model = Image.open(directory+'model.png')
    template = Image.open(directory+'templates\\beautiful.png')
    model_ratio = model.width / model.height
    x_side = 494 - 367
    y_side = 182 - 40
    template_ratio = x_side / y_side
    if model_ratio > template_ratio:
        new_height = int(127 // model_ratio)
        canvas = model.resize((127, new_height))
        adjust = (142 - new_height) // 2
        template.paste(canvas, (367, 40 + adjust))
        template.paste(canvas, (370, 326 + adjust))
    else:
        new_width = int(142 * model_ratio)
        canvas = model.resize((new_width, 142))
        adjust = (127 - new_width) // 2
        template.paste(canvas, (367 + adjust, 40))
        template.paste(canvas, (370 + adjust, 326))
    template.save(directory+'art.png', "PNG")
    art = open(directory+'art.png', 'rb')
    return file(art)


def draw_caption(img, text, top=False, padding=10):
    draw = ImageDraw.Draw(img)
    # Find a suitable font size to fill the entire width:
    w = img.size[0]
    s = 50
    h = 0
    font = ImageFont.truetype('impact.ttf', s)
    while w >= (img.size[0] - 20):
        font = ImageFont.truetype('impact.ttf', s)
        w, h = draw.textsize(text, font=font)
        s -= 1
        if s <= 12:
            break

    draw_x = (img.size[0] - w) / 2

    # Draw the text multiple times in black to get the outline:
    for x in range(-3, 4):
        for y in range(-3, 4):
            draw_y = y + padding if top else img.size[1] - h + y - padding
            draw.text((draw_x + x, draw_y), text, font=font, fill='black')
    # Draw the text once more in white:
    draw_y = 0 + padding if top else img.size[1] - h - padding
    draw.text((draw_x, draw_y), text, font=font, fill='white')


def meme(user: discord.Member, get_text: str):
    full_text = get_text
    if '@{}'.format(user.display_name.lower()) in get_text:
        partial_text = full_text.split('@{}'.format(user.display_name.lower()))
        partial_text.remove('')
        full_text = partial_text[0]
    if ',' in full_text:
        text = full_text.split(',')
        upper_text = text[0]
        lower_text = text[1]
    else:
        upper_text = full_text
        if len(full_text.split()) >= 2:
            text_split = full_text.split()
            upper_text = " ".join(text_split[:(len(full_text.split()) // 2)])
            lower_text = " ".join(text_split[(len(full_text.split()) // 2):])
        else:
            lower_text = ' '
    upper_text = upper_text.upper()
    lower_text = lower_text.upper()
    url = requests.get(user.avatar_url).content
    with open(directory+'base.png', 'wb+') as avatar:
        avatar.write(url)
    base = Image.open(directory+'base.png').resize((300, 300))
    draw_caption(base, upper_text, top=True, padding=3)
    draw_caption(base, lower_text, top=False, padding=20)
    base.save(directory+'meme.png', 'PNG')
    m = open(directory+'meme.png', 'rb')
    return file(m)


def cinnamon(message):
    # For people who are too pure for this world
    has_url = False
    for content in message.content.split():
        if '.png' in content or '.jpg' in content:
            url = requests.get(content).content
            with open(directory + 'sugar.png', 'wb+') as sugar:
                sugar.write(url)
                has_url = True
    if has_url:
        pass
    elif len(message.attachments) != 0:
        message.attachments[0].save(directory+'sugar.png')
    elif len(message.mentions) != 0:
        avatar = requests.get(message.mentions[0].avatar_url).content
        with open(directory+'sugar.png', 'wb+') as sugar:
            sugar.write(avatar)
    else:
        avatar = requests.get(message.author.avatar_url).content
        with open(directory+'sugar.png', 'wb+') as sugar:
            sugar.write(avatar)
    dough = Image.open(directory+'sugar.png')
    roll = Image.open(directory+'templates\\cinnamon.png')
    dough_ratio = dough.width / dough.height
    roll_ratio = (530 - 20) / (590 - 110)
    if dough_ratio > roll_ratio:
        new_height = int((530-20) // dough_ratio)
        cinnamon_roll = dough.resize(((530-20), new_height))
    else:
        new_width = int((590 - 110) * dough_ratio)
        cinnamon_roll = dough.resize((new_width, (590 - 110)))

    # 20,110,530,590
    side1 = cinnamon_roll.width
    side2 = roll.width
    cd = (side2 - side1) // 2

    down = (590 - 110 - cinnamon_roll.height) // 2

    roll.paste(cinnamon_roll, (cd, 110 + down))
    roll.save(directory+'cinnamon_roll.png', "PNG")
    cr = open(directory+'cinnamon_roll.png', 'rb')
    return file(cr)
