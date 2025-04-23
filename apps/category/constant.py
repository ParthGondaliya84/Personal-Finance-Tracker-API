from collections import OrderedDict


class CategoryType:
    INCOME = 'income'
    EXPENSE = 'expense'

    FileStr = OrderedDict({
        INCOME: 'Income',
        EXPENSE: 'Expense'
    })

    @classmethod
    def choice(cls):
        return list(cls.FileStr.items())
