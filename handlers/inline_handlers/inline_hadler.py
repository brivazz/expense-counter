from aiogram.types import CallbackQuery

from utils.create_bot import dp, bot
from messages.inline_buttons_messages.inline_messages import products_msg, telephone_msg, other_msg
from messages.inline_buttons_messages.start_message import start_msg
from keyboards.inline_keyboards.menu_keyboards import menu_keyboard, back_buttons
from keyboards.inline_keyboards.start_menu import start_kb
from database.sqlite_db import save_to_db


@dp.callback_query_handler(text='save_amount')
async def save_amounts(call: CallbackQuery):
    await call.answer('Записано', show_alert=True)
    await save_to_db(call)


@dp.callback_query_handler(text='back_btn')
async def back(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=start_msg(call.from_user.full_name),
        reply_markup=start_kb
    )


@dp.callback_query_handler(
    text=[
        'products_btn', 'telephone_btn', 'other_btn',
        'back_to_products', 'back_to_telephone','back_to_other',
        'plus', 'minus',
        'back_from_show', 'back_from_show_telephone', 'back_from_show_other'
    ])
async def products(call: CallbackQuery):
    await call.answer()
    if call.data in ['products_btn', 'back_to_products', 'back_from_show']:
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=products_msg,
            reply_markup=await menu_keyboard(call)
        )
    elif call.data in ['telephone_btn', 'back_to_telephone', 'back_from_show_telephone']:
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=telephone_msg,
            reply_markup=await menu_keyboard(call)
        )
    elif call.data in ['other_btn', 'back_to_other', 'back_from_show_other']:
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=other_msg,
            reply_markup=await menu_keyboard(call)
        )
    elif call.data in ['plus', 'minus']:
        if call['message']['text'] == 'Продукты':
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=products_msg,
                reply_markup=await menu_keyboard(call)
            )
        elif call['message']['text'] == 'Телефон':
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=telephone_msg,
                reply_markup=await menu_keyboard(call)
            )
        elif call['message']['text'] == 'Другие расходы':
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=other_msg,
                reply_markup=await menu_keyboard(call)
            )
