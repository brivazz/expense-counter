from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.create_bot import dp, bot
from database.sqlite_db import from_db, show_month, show_all
from keyboards.inline_keyboards.show_report_keyboards import show_report, back_from_sum


@dp.callback_query_handler(text='show_report')
async def show_reports(call: CallbackQuery):
    print(call.data, call.message.text)
    await call.answer()
    if call.message.text == 'Продукты':
        await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=call.message.text,
                reply_markup=await show_report(call.message.text)
        )
    elif call.message.text == 'Телефон':
        await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=call.message.text,
                reply_markup=await show_report(call.message.text)
        )
    elif call.message.text == 'Другие расходы':
        await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=call.message.text,
                reply_markup=await show_report(call.message.text)
        )


@dp.callback_query_handler(text=['show_month', 'show_all'])
async def show_expense(call: CallbackQuery):
    await call.answer()
    if call.data == 'show_month':
        result = await show_month(call)
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=call.message.text + ': ' + hbold(result) + ' рублей',
            reply_markup=await back_from_sum(call.message.text)
        )
    elif call.data == 'show_all':
        result = await show_all(call)
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=call.message.text + ': ' + hbold(result) + ' рублей',
            reply_markup=await back_from_sum(call.message.text)
        )


@dp.callback_query_handler(text=[
    'back_from_sum_products', 'back_from_sum_telephone', 'back_from_sum_other'])
async def back_from_sum_callback(call: CallbackQuery):
    await call.answer()
    if call.data == 'back_from_sum_products':
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text='Продукты',
            reply_markup=await show_report('Продукты')
        )
    elif call.data == 'back_from_sum_telephone':
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text='Телефон',
            reply_markup=await show_report('Телефон')
        )
    elif call.data == 'back_from_sum_other':
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text='Другие расходы',
            reply_markup=await show_report('Другие расходы')
        )
