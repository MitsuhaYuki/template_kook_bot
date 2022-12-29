import logging
import random
from khl import Bot, Message
from khl.card import Card, CardMessage, Module, Types, Struct
from typing import Dict
from src.utils import check_role_admin
from . import ping, example, dev, card

log = logging.getLogger('custom.bot')

# register handlers, this will be use for generate main menu!
apps = [{
    'title': 'Builtin Commands',
    'theme': Types.Theme.SECONDARY,
    'routers': [{
        'prefix': 'hi',
        'desc': 'Ping Command',
        'route': ping
    }, {
        'prefix': 'exp',
        'desc': 'handler example',
        'route': example
    }]
}, {
    'title': 'Admin Commands',
    'theme': Types.Theme.SECONDARY,
    'routers': [{
        'prefix': 'dev',
        'desc': 'auth & role check',
        'route': dev
    }]
}, {
    'title': 'HIDDEN',  # this router will be hidden from the main menu!
    'theme': Types.Theme.SECONDARY,
    'routers': [{
        'prefix': 'el',
        'desc': 'this menu will hide!',
        'route': card
    }]
}]


def reg_all_handler(bot: Bot, config: Dict, env: Dict):
    """
    generate main menu and register all endpoint command routers
    :param bot: khl.py Bot
    :param config: config file
    :param env: runtime env vars
    :return: None
    """
    cm = CardMessage(Card(Module.Header('Available Commands'), theme=Types.Theme.PRIMARY))
    log.info('registering apps...')
    for app in apps:
        cate_card = Card(
            Module.Context(app.get('title', '*ERROR*')),
            theme=app.get('theme', Types.Theme.SECONDARY)
        )
        for route in app.get('routers', []):
            if route.get('route', None) is not None:  # If it has a handler, register it.
                log.info(f'route {route.get("prefix")} is now registered')
                route['route'].handler(route.get('prefix', f'tmp{random.randint(0, 9999)}'), bot, config, env)
            cate_card.append(Module.Section(
                Struct.Paragraph(2, f"/{route.get('prefix', '*ERROR*')}", route.get('prefix', '*ERROR*'))
            ))
        if app.get('title') != 'HIDDEN':
            cm.append(cate_card)

    @bot.command(name='help')
    async def main_menu(msg: Message):
        if not await check_role_admin(msg, bot):
            return
        await msg.reply(cm, is_temp=True)

    @bot.command(name='*ERROR*')
    async def error_cmd(msg: Message):
        await msg.reply('Command not available yet!', is_temp=True)
