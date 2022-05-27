from aiogram import executor

from utils.create_bot import dp, bot
from utils.notify_admins import on_startup_notify  # , on_shutdown_notify
from utils.set_bot_commands import set_default_commands
import handlers
from database.models import create_tables, fields_expense


async def on_startup(dp):
    # Устанавливает команды бота
    await set_default_commands(dp)
    # Уведомляет администратора про запуск бота
    await on_startup_notify(dp)
    await create_tables()
    await fields_expense()


async def on_shutdown(dp):
    # await on_shutdown_notify(dp)
    pass


if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True
    )
