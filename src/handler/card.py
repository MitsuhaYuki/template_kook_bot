from khl import Bot, Message, EventTypes, Event
from khl.card import Card, CardMessage, Module, Element, Types, Struct
from typing import Dict
from datetime import datetime, timedelta
from src.utils import render_sub_menu

"""
Example File - Card message example
"""


def handler(prefix: str, bot: Bot, config: Dict, env: Dict):
    @bot.command(name=prefix)
    async def sub_menu(msg: Message):
        menu = {
            'title': 'Element Example',
            'cmds': {
                f'{prefix}': 'show this menu',
                f'{prefix}a': 'card msg example'
            }
        }
        await msg.reply(render_sub_menu(menu['title'], menu['cmds']), is_temp=True)

    @bot.command(name=f'{prefix}a')
    async def hi_func(msg: Message):
        cm = CardMessage()

        c1 = Card(
            Module.Header('Header'),
            # 1 Section can only have 1 Struct
            Module.Section(Struct.Paragraph(3, 'Col1', 'Col2', 'Col3')),
            Module.Divider(),  # a divider
            Module.Context('Context?'),  # a description text
            Module.Section('Section?'),  # a normal text
            # Button group
            Module.ActionGroup(
                Element.Button('TEXT', 'someValue', theme=Types.Theme.INFO),
                Element.Button('TEXT2', 'someValue2')
            ),
            # Button with link
            Module.Section(
                'To Link',
                Element.Button('Home', 'https://www.baidu.com', Types.Click.LINK),
            ),
            # Countdowns with various mode
            Module.Countdown(datetime.now() + timedelta(seconds=10), mode=Types.CountdownMode.SECOND),
            Module.Countdown(datetime.now() + timedelta(seconds=10), mode=Types.CountdownMode.HOUR),
            Module.Countdown(datetime.now() + timedelta(seconds=10), mode=Types.CountdownMode.DAY),
            # Invite card
            Module.Invite('iwQXrG')
        )

        c2 = Card(
            Module.Section('Card2'),
            color='#ff0000',
            theme=Types.Theme.INFO
        )
        cm.append(c1)
        cm.append(c2)
        await msg.reply(cm, is_temp=True)

    # button click event handle
    @bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
    async def print_btn_value(_: Bot, e: Event):
        print(f'''{e.body['user_info']['nickname']} click on {e.body['value']} btn''')
