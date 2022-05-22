from rest_framework import serializers
from .models import Income

class IncomeSerializer(serializers.ModelSerializer):
    
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        model=Income
        fields = ['id', 'date',  'description', 'amount', 'source']