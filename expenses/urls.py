from django.urls import path, include
from . import views

urlpatterns = [  
    path('', views.ExpenseListAPIView.as_view(), name="expenses"),    
    path('<int:id>', views.ExpenseDetailAPIView.as_view(), name="expense"),           
]