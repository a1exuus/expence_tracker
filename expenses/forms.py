from django import forms
from .models import Expense, ExpenseCategory, Income, IncomeCategory


class ExpenseForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=ExpenseCategory.objects.all(),
        required=True,
        empty_label='Выберите категорию',
        label='Категория'
    )

    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description']
        labels = {
            'amount': 'Сумма',
            'description': 'Описание',
            'category': 'Категория'
        }


class IncomeForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=IncomeCategory.objects.all(),
        required=True,
        empty_label='Выберите категорию',
        label='Категория'
    )

    class Meta:
        model = Income
        fields = ['category', 'amount', 'description']
        labels = {
            'amount': 'Сумма',
            'description': 'Описание',
        }
