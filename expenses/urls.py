from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions_list, name='index'),
    path('income/add/', views.income_add, name='income_add'),
    path('income/edit/<int:pk>', views.income_edit, name='income_edit'),
    path('income/delete/<int:pk>', views.income_delete, name='income_delete'),
    path('expense/add/', views.expense_add, name='expense_add'),
    path('expense/edit/<int:pk>/', views.expense_edit, name='expense_edit'),
    path('expense/delete/<int:pk>/', views.expense_delete, name='expense_delete'),
]
