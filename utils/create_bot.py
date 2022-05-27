import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from .config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
)
