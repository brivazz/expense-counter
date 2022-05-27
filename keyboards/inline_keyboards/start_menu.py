from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Клавиатура после нажатия "/start"
start_kb = InlineKeyboardMarkup(row_width=2)

products_btn = InlineKeyboardButton(
                text='Продукты',
                callback_data='products_btn'
            )
telephone_btn = InlineKeyboardButton(
    text='Телефон',
    callback_data='telephone_btn'
)
other_btn = InlineKeyboardButton(
    text='Другие расходы',
    callback_data='other_btn'
)
start_kb.add(products_btn, telephone_btn, other_btn)
