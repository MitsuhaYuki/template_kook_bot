from khl import Bot
from src.handler import reg_all_handler
import json
import logging
import os

# init logging service
logging.basicConfig(level='INFO')
log = logging.getLogger('custom.bot')

# read config file
log.info(f"current workspace is {os.getcwd()}")
with open(f'{os.getcwd()}/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# init Bot
bot = Bot(config['token'])

# runtime parameters
env = {}

reg_all_handler(bot, config, env)
