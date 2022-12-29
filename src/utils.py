from khl import Bot, Message
from khl.card import CardMessage, Card, Module, Struct
import os
import json
import logging

log = logging.getLogger('custom.bot')

with open(f'{os.getcwd()}/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)


async def check_sys_admin(msg: Message) -> bool:
    """
    check if current msg author has enough permission with system config
    :param msg: khl.py Message
    :return: bool
    """
    if msg.author.id not in config['admin_users']:
        await msg.reply('Permission Denied!', is_temp=True)
        log.error(f'access denied for {msg.author.nickname}({msg.author.id})')
        return False
    else:
        return True


async def check_role_admin(msg: Message, bot: Bot) -> bool:
    """
    check if current msg author has enough permission with system config
    :param msg: khl.py Message
    :return: bool
    """
    server = await bot.client.fetch_guild(msg.guild.id)
    cur_user = await server.fetch_user(msg.author.id)
    result_roles = list(set(cur_user.roles).intersection(set(config.get("admin_roles"))))
    if len(result_roles) > 0:
        return True
    else:
        await msg.reply('You do not have correct role for executing this command!', is_temp=True)
        return False


def render_sub_menu(title='*Not Set*', cmds=None) -> CardMessage:
    """
    function to generate second level command menu
    :param title: submenu title
    :param cmds: commands with its description
    :return: khl.py CardMessage
    """
    if cmds is None:
        cmds = {}
    cm = CardMessage()
    c1 = Card(
        Module.Header(title),
        Module.Divider(),
        Module.Context('*Not Set*'),
    )
    for key in cmds:
        c1.append(Module.Section(Struct.Paragraph(2, f'/{key}', cmds[key])))
    cm.append(c1)
    return cm
