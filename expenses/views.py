from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense, Income
from .forms import ExpenseForm, IncomeForm
from itertools import chain
from operator import attrgetter


def transactions_list(request):
    expenses = Expense.objects.all()
    incomes = Income.objects.all()

    for e in expenses:
        e.type = 'Расход'
    for i in incomes:
        i.type = 'Доход'

    transactions = sorted(
        chain(expenses, incomes),
        key=attrgetter('date'),
        reverse=True
    )

    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_income = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    return render(request, 'expenses/transactions_list.html', {
        'transactions': transactions,
        'total_expense': total_expense,
        'total_income': total_income,
        'balance': balance,
    })


def income_add(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IncomeForm()

    return render(request, 'expenses/income_form.html', {'form': form})


def income_edit(request, pk):
    income = get_object_or_404(Income, pk=pk)

    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IncomeForm(instance=income)

    return render(request, 'expenses/income_form.html', {'form': form})


def income_delete(request, pk):
    income = get_object_or_404(Income, pk=pk)

    if request.method == "POST":
        income.delete()
        return redirect('index')

    return render(
        request,
        'expenses/income_confirm_delete.html',
        {'income': income}
        )


def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/expense_form.html', {'form': form})


def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/expense_form.html', {'form': form})


def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == "POST":
        expense.delete()
        return redirect('index')

    return render(
        request,
        'expenses/expense_confirm_delete.html',
        {'expense': expense}
        )
