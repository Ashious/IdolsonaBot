import discord
import os
import io
from ProjectIdolsona import IdolsonaInfo

filename = r'C:\Users\Hp\PycharmProjects\ProjectIdolsona\bot'
client = discord.Client(max_messages=10000)
owner_list = IdolsonaInfo.owners()


def check_for_tag(idolsona, tag_name: str, author: discord.Member):
    final_directory = filename+'\\{}\\tags'.format(idolsona)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
        with open(filename+'\\{}\\tag_list.txt'.format(idolsona), 'w+') as create_new:
            create_new.write('')
    with open(filename+'\\owner_list.txt') as owner_list:
        authors = owner_list.read().split('\n')
        if str(author.id) not in authors:
            with open(filename + '\\owner_list.txt', 'a+') as new_author, \
                    open(filename+'\\creators\\{}.txt'.format(author.id), 'w') as new_author_list:
                new_author.write(str(author.id) + '\n')
                new_author_list.write('')
    with open(filename+'\\{}\\tag_list.txt'.format(idolsona)) as get_tags:
        tag_list = get_tags.read().split('\n')
    if tag_name in tag_list:
        exist = True
    else:
        exist = False
    return exist


def tag_create(idolsona: str, tag_name: str, content: str, owner: discord.Member):
    if check_for_tag(idolsona, tag_name, owner):
        return '**{}:** I already have that tag!'.format(idolsona)
    else:
        final_directory = filename+'\\{}\\tags\\'.format(idolsona)
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        with open(filename+'\\{}\\tags\\{}.txt'.format(idolsona, tag_name), 'w+') as form_tag,\
                open(filename+'\\{}\\tag_list.txt'.format(idolsona), 'a+') as tag_list, \
                open(filename+'\\creators\\{}.txt'.format(owner.id), 'a+') as owner_tag_list:
            tag_list.write(tag_name+'\n')
            owner_tag_list.write("{},{}\n".format(idolsona, tag_name))
            form_tag.write(str(owner.id)+'\n'+content)
        return 'Your tag has been created!'


def tag_edit(idolsona: str, tag_name: str, editor: discord.Member, edit_content: str):
    if check_for_tag(idolsona, tag_name, editor):
        with open(filename+'\\{}\\tags\\{}.txt'.format(idolsona, tag_name)) as from_tag:
            check_for_owner = from_tag.read().split('\n')[0]
        editor_id = 'default'
        if str(editor.id) in owner_list:
            editor_id = str(editor.id)
        if str(editor.id) == check_for_owner or idolsona in owner_list[editor_id]:
            with io.open(filename+'\\{}\\tags\\{}.txt'.format(idolsona, tag_name), 'w+') as from_tag:
                from_tag.write(str(editor.id)+'\n'+edit_content)
            return 'Tag edited!'
        else:
            return 'You cannot edit this tag!'
    else:
        return 'This tag does not exist!'


def get_tag(idolsona, tag_name, author: discord.Member):
    if check_for_tag(idolsona, tag_name, author):
        with open(filename+'\\{}\\tags\\{}.txt'.format(idolsona, tag_name)) as content:
            from_tag = content.read().split('\n')
            return '\n'.join(from_tag[1:])
    else:
        return 'This tag does not exists!'


def get_author(idolsona: str, tag_name: str, author: discord.Member, guild:discord.Guild):
    if not check_for_tag(idolsona, tag_name, author):
        return 'This tag does not exists!'
    else:
        with open(filename + '\\{}\\tags\\{}.txt'.format(idolsona, tag_name)) as from_tag:
            owner_id = from_tag.read().split('\n')[0]
        owner = guild.get_member(int(owner_id))
        return 'This tag is from '+owner.name+'!'


def get_author_tags(author: discord.Member, idolsona: str, escape: str):
    with open(filename+'\\owner_list.txt') as owner_list:
        owners = owner_list.read().split('\n')
        idol = idolsona
        if idolsona == 'all':
            idol = escape
        if str(author.id) in owners:
            with open(filename+'\\creators\\{}.txt'.format(author.id)) as author_tag_list:
                author_tags = author_tag_list.read().split('\n')
            if len(author_tags) == 0:
                return "**{}:** {} do not have any tags!".format(idol, author.name)
            author_tags.remove(author_tags[-1])
            if len(author_tags) == 0:
                return "**{}:** {} do not have any tags!".format(idol, author.name)
            else:
                tags_list = {}
                for tags in author_tags:
                    tag = tags.split(',')
                    idol_name = tag[0]
                    if idol_name not in tags_list:
                        tags_list[idol_name] = []
                    individuals = tags_list[idol_name]
                    individuals.append(tag[1])
                    tags_list[idol_name] = individuals
                if idolsona == 'all':
                    all_tags = []
                    idolsona_tags = tags_list.keys()
                    for idols in idolsona_tags:
                        all_tags.append("**{}:** {}".format(idols, ",".join(tags_list[idols])))
                    return "```{}'s tags:```{}".format(author.name, "\n".join(all_tags))
                else:
                    if idol not in tags_list:
                        return "**{}:** I do not have any tags from {}!".format(idolsona, author.name)
                    tag_pair = tags_list[idol]
                    if len(tag_pair) == 0:
                        return "**{}:** I do not have any tags from {}!".format(idolsona, author.name)
                    else:
                        user_idolsona_tags = ", ".join(tag_pair)
                        return "```{}'s tags for {}:```{}".format(author.name, idol, user_idolsona_tags)
        else:
            return "**{}:** {} do not have any tags!".format(idol, author.name)


def get_tag_list(idolsona: str, author: discord.Member):
    if not check_for_tag(idolsona, 'a name tag that no one will use', author):
        with open(filename + '\\{}\\tag_list.txt'.format(idolsona)) as tag_list:
            all_tags = tag_list.read().split('\n')
            all_tags.remove('')
            tags = ", ".join(all_tags)
            return "```{}'s tags```{}".format(idolsona, tags)
    else:
        return 'Ash notes: idk how you managed to get this message wtf'


def tag_delete(idolsona: str, tag_name: str, editor: discord.Member):
    if check_for_tag(idolsona, tag_name, editor):
        with open(filename+'\\{}\\tags\\{}.txt'.format(idolsona, tag_name)) as from_tag, \
                open(filename+'\\{}\\tag_list.txt'.format(idolsona)) as get_tags, \
                open(filename+'\\creators\\{}.txt'.format(editor.id)) as get_owner_tags:
            current_list = get_tags.read().split('\n')
            owner_tags = get_owner_tags.read().split('\n')
            check_for_owner = from_tag.read().split('\n')[0]
        editor_id = 'default'
        if str(editor.id) in owner_list:
            editor_id = str(editor.id)
        if str(editor.id) == check_for_owner or idolsona in owner_list[editor_id]:
            with open(filename+'\\{}\\tags\\{}.txt'.format(idolsona, tag_name), 'w+') as from_tag, \
                    open(filename+'\\{}\\tag_list.txt'.format(idolsona), 'w') as tag_list,\
                    open(filename+'\\creators\\{}.txt'.format(editor.id), 'w') as owner_tag_list:
                current_list.remove(tag_name)
                owner_tags.remove(idolsona+','+tag_name)
                tag_list.write('\n'.join(current_list))
                owner_tag_list.write('/n'.join(owner_tags))
                from_tag.write('*null*')
                return 'Tag deleted!'
        else:
            return 'You cannot delete this tag!'
    else:
        return 'This tag does not exist!'


'''For debugging purposes:
temp_id = input('Enter ID: ')
signal = input('Start? ')
while signal == 'yes':
    name = input('Enter name: ')
    action = input('What do you want to do? ')
    if action.lower() == 'create':
        tag = input('Enter tag name: ')
        new_tag = input('Enter content: ')
        print(tag_create(name, tag, new_tag, temp_id))
    elif action.lower() == 'get':
        tag = input('Enter tag name: ')
        print(get_tag(name, tag))
    elif action.lower() == 'delete':
        tag = input('Enter tag name: ')
        print(tag_delete(name, tag, temp_id))
    elif action.lower() == 'edit':
        tag = input('Enter tag name: ')
        new_content = input('Enter new content: ')
        print(tag_edit(name, tag, temp_id, new_content))
    else:
        print('Not an available action name.')
    signal = input('Continue? ')
'''
