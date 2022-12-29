from khl import Bot, Message
from typing import Dict
from src.utils import check_sys_admin, check_role_admin, render_sub_menu

"""
Example File - Role check example
"""


def handler(prefix: str, bot: Bot, config: Dict, env: Dict):
    @bot.command(name=prefix)
    async def sub_menu(msg: Message):
        menu = {
            'title': 'Hide Menu',
            'cmds': {
                f'{prefix}': 'Show This Menu',
                f'{prefix}auth': 'Auth',
                f'{prefix}role': 'Role'
            }
        }
        await msg.reply(render_sub_menu(menu['title'], menu['cmds']), is_temp=True)

    @bot.command(name=f'{prefix}auth')
    async def dev_admin_check(msg: Message):
        if await check_sys_admin(msg):
            await msg.reply('Pass', is_temp=True)
        else:
            await msg.reply('Reject', is_temp=True)

    @bot.command(name=f'{prefix}role')
    async def dev_admin_check(msg: Message):
        if await check_role_admin(msg, bot):
            await msg.reply('Pass', is_temp=True)
        else:
            await msg.reply('Reject', is_temp=True)
