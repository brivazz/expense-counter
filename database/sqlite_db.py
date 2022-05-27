import datetime
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
                [res.amount, datetime.datetime.strftime(res.payment_date, '%d.%m.%Y')])
    return res_list


async def show_month(call):
    month = datetime.date.today()
    now_month = str(month).split('-')[1]
    my_list = []
    count = 0
    with db:
        query = Expense.get(Expense.product_name == call.message.text)
        print(query)
        date = Payment.select().where(Payment.expense_id == query)
        for d in date:
            num = str(d.payment_date).split('-')[1]
            if num == now_month:
                count += d.amount
        my_list.append(count)

    return count


async def show_all(call):
    with db:
        query = Expense.get(Expense.product_name == call.message.text)
        print(query)
        result = Payment.select().where(Payment.expense_id == query)
        count = 0
        for res in result:
            count += res.amount
    return count
