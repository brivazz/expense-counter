import datetime
from peewee import IntegrityError
from peewee import (SqliteDatabase, Model,
                    CharField, DateTimeField,
                    IntegerField, ForeignKeyField)


db = SqliteDatabase('expense_payments.db')


class BaseModel(Model):
    class Meta:
        database = db


class Expense(BaseModel):
    product_name = CharField(max_length=50, unique=True)

    class Meta:
        table_name = 'expenses'


class Payment(BaseModel):
    amount = IntegerField()
    payment_date = DateTimeField(default=datetime.date.today())
    expense_id = ForeignKeyField(Expense)  # , field=Expense.product_name

    class Meta:
        table_name = 'payments'


async def create_tables():
    with db:
        db.create_tables([Expense, Payment])


async def fields_expense():
    fields_expense = [
        {'product_name': 'Продукты'},
        {'product_name': 'Телефон'},
        {'product_name': 'Другие расходы'}
    ]
    with db:
        try:
            Expense.insert(fields_expense).execute()
        except IntegrityError:
            pass
