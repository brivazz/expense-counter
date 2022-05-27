from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.create_bot import dp, bot
from messages.inline_buttons_messages.start_message import start_msg
from keyboards.inline_keyboards.start_menu import start_kb


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id
    )
    await message.answer(
        text=start_msg(message.from_user.full_name),
        reply_markup=start_kb
    )
