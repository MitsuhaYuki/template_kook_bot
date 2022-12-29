from khl import Bot, Message
from typing import Dict
from datetime import datetime
from src.utils import check_role_admin, render_sub_menu


def handler(prefix: str, bot: Bot, config: Dict, env: Dict):
    """
    actual handler for handle user input commands, refers to khl.py
    :param prefix: commands prefix in this router
    :param bot: khl.py Bot
    :param config: config file
    :param env: runtime env vars
    :return: None
    """
    @bot.command(name=prefix)
    async def sub_menu(msg: Message):
        # TODO: uncomment below if you need authentication!
        # if not await check_role_admin(msg, bot):
        #     return
        menu = {
            'title': 'Example Menu',
            'cmds': {
                f'{prefix}': 'Show this menu',
                f'{prefix}a': 'Example cmd A'
            }
        }
        await msg.reply(render_sub_menu(menu['title'], menu['cmds']), is_temp=True)

    @bot.command(name=f'{prefix}a')
    async def command_func(msg: Message):
        # TODO: uncomment below if you need authentication!
        # if not await check_role_admin(msg, bot):
        #     return
        await msg.reply(f'Example cmd, now is {datetime.now()}', is_temp=True)
