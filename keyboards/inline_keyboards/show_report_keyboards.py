from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def show_report(call):
    show_report_kb = InlineKeyboardMarkup()
    show_month_btn = InlineKeyboardButton(
        text='Расходы за месяц',
        callback_data='show_month'
    )
    show_all_btn = InlineKeyboardButton(
        text='Все расходы',
        callback_data='show_all'
    )
    if call == 'Продукты':
        back_btn = InlineKeyboardButton(
            text='Назад',
            callback_data='back_from_show_products'
        )
    elif call == 'Телефон':
        back_btn = InlineKeyboardButton(
            text='Назад',
            callback_data='back_from_show_telephone'
        )
    elif call == 'Другие расходы':
        back_btn = InlineKeyboardButton(
            text='Назад',
            callback_data='back_from_show_other'
        )
    show_report_kb.add(show_month_btn, show_all_btn)
    show_report_kb.add(back_btn)
    return show_report_kb


async def back_from_sum(call):
    back_from_sum_kb = InlineKeyboardMarkup()
    if call == 'Продукты':
        back_btn = InlineKeyboardButton(
            text='Назад',
            callback_data='back_from_sum_products'
        )
    elif call == 'Телефон':
        back_btn = InlineKeyboardButton(
            text='Назад',
            callback_data='back_from_sum_telephone'
        )
    elif call == 'Другие расходы':
        back_btn = InlineKeyboardButton(
            text='Назад',
            callback_data='back_from_sum_other'
        )
    back_from_sum_kb.add(back_btn)
    return back_from_sum_kb
