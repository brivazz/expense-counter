from aiogram import Dispatcher

from .config import MY_ID


async def on_startup_notify(dp: Dispatcher):
    if MY_ID:
        await dp.bot.send_message(
            text='Бот запущен',
            chat_id=MY_ID,
            disable_notification=True
        )


async def on_shutdown_notify(dp: Dispatcher):
    if MY_ID:
        await dp.bot.send_message(
            text='Бот упал',
            chat_id=MY_ID,
            disable_notification=True
        )
