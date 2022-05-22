from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        model=Expense
        fields = [ 'id',  'date',  'description', 'amount', 'category']