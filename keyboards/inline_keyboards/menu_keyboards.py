from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def menu_keyboard(call):
    print('v klaviature menu_keyboard=', call.data)
    data = call['data']
    if data == 'plus':
        data = int(call['message']['reply_markup']['inline_keyboard'][0][1]['text'])
        data += 10
        sum_btn = InlineKeyboardButton(
            text=data,
            callback_data=data
        )
    elif data == 'minus':
        data = int(call['message']['reply_markup']['inline_keyboard'][0][1]['text'])
        data -= 10
        sum_btn = InlineKeyboardButton(
            text=data,
            callback_data=data
        )
    else:
        sum_btn = InlineKeyboardButton(
            text='300',
            callback_data=300
        )

    products_kb = InlineKeyboardMarkup(row_width=3)
    plus_btn = InlineKeyboardButton(
        text='+',
        callback_data='plus'
    )
    minus_btn = InlineKeyboardButton(
        text='-',
        callback_data='minus'
    )
    save_btn = InlineKeyboardButton(
        text='Записать',
        callback_data='save_amount'
    )
    back_btn = InlineKeyboardButton(
        text='Назад',
        callback_data='back_btn'
    )
    show_report_btn = InlineKeyboardButton(
        text='Показать записи',
        callback_data='show_report'
    )

    products_kb.add(plus_btn, sum_btn, minus_btn, save_btn)
    products_kb.add(show_report_btn)
    products_kb.add(back_btn)

    return products_kb


async def back_buttons(call):
    back_kb = InlineKeyboardMarkup()

    if call == 'Продукты':
        back_btn = InlineKeyboardButton(text='Назад', callback_data='back_to_products')
        back_kb.add(back_btn)
        return back_kb

    elif call == 'Телефон':
        back_btn = InlineKeyboardButton(text='Назад', callback_data='back_to_telephone')
        back_kb.add(back_btn)
        return back_kb

    elif call == 'Другие расходы':
        back_btn = InlineKeyboardButton(text='Назад', callback_data='back_to_other')
        back_kb.add(back_btn)
        return back_kb
