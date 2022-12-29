from khl import Bot, Message
from typing import Dict


def handler(prefix: str, bot: Bot, config: Dict, env: Dict):
    @bot.command(name=prefix)
    async def hi_func(msg: Message):
        await msg.reply('Hi!', is_temp=True)
