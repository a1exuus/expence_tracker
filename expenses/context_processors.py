from django.db.models import Sum
from .models import Expense, Income


def balance_context(request):
    total_income = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense
    return {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
