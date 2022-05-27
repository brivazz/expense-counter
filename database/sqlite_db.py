from datetime import datetime
from .models import db, Expense, Payment


async def save_to_db(call):
    with db.atomic():
        query = Expense.get(Expense.product_name == call.message.text)
        Payment.create(
            amount=int(
                call['message']['reply_markup']['inline_keyboard'][0][1]['text']),
            expense_id=query
        )


async def from_db(call):
    res_list = []
    with db:
        query = Expense.get(Expense.product_name == call.message.text)
        result = (Payment.select().where(
                    Payment.expense_id == query).order_by(
                        Payment.payment_date.desc()))
        for res in result:
            res_list.append(
                [res.amount, datetime.strftime(res.payment_date, '%d.%m.%Y')])
    return res_list
