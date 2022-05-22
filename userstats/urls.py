from .views import ExpenseSummaryStats, IncomeSourcesSummaryStats
from django.urls import path 

urlpatterns = [
    path('expense_category_data', ExpenseSummaryStats.as_view(), name="expense-category-data"),
    path('income_sources_data', IncomeSourcesSummaryStats.as_view(), name="income-sources-data")
    
]