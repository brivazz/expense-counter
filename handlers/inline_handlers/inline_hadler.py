from datetime import datetime
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold, hlink

from utils.create_bot import dp, bot
from messages.inline_buttons_messages.inline_messages import products_msg, telephone_msg, other_msg
from messages.inline_buttons_messages.start_message import start_msg
from keyboards.inline_keyboards.menu_keyboards import menu_keyboard, back_buttons
from keyboards.inline_keyboards.start_menu import start_kb
from database.sqlite_db import from_db, save_to_db


@dp.callback_query_handler(text='save_amount')
async def save_amounts(call: CallbackQuery):
    await call.answer()
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


@dp.callback_query_handler(text='show_report')
async def show_reports(call: CallbackQuery):
    print(call.data, call.message.text)
    await call.answer()
    result = await from_db(call)
    if call.message.text == 'Продукты':
        res_text = hbold('=== Продукты ===\n\n')
        for res in result:
            result = f"Сумма: {res[0]}\nДата: {res[1]}\n\n"
            res_text += result
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=res_text,
                reply_markup=await back_buttons(call.message.text)
            )
    elif call.message.text == 'Телефон':
        res_text = hbold('=== Телефон ===\n\n')
        for res in result:
            result = f"Сумма: {res[0]}\nДата: {res[1]}\n\n"
            res_text += result
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=res_text,
                reply_markup=await back_buttons(call.message.text)
            )
    elif call.message.text == 'Другие расходы':
        res_text = hbold('=== Другие расходы ===\n\n')
        for res in result:
            result = f"Сумма: {res[0]}\nДата: {res[1]}\n\n"
            res_text += result
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=res_text,
                reply_markup=await back_buttons(call.message.text)
            )


@dp.callback_query_handler(
    text=[
        'products_btn', 'telephone_btn', 'other_btn',
        'back_to_products', 'back_to_telephone',
        'back_to_other', 'plus', 'minus'
    ])
async def products(call: CallbackQuery):
    await call.answer()
    if call.data in ['products_btn', 'back_to_products']:
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=products_msg,
            reply_markup=await menu_keyboard(call)
        )
    elif call.data in ['telephone_btn', 'back_to_telephone']:
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=telephone_msg,
            reply_markup=await menu_keyboard(call)
        )
    elif call.data in ['other_btn', 'back_to_other']:
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
