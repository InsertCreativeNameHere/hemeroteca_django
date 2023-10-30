from rest_framework import serializers
from .models import loan

class loanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = loan
        fields = '__all__'
    
    
    def is_valid(self, raise_exception=False):
        
        data = self.initial_data
        
        _loans = loan.objects.filter(copy_id = data.get("copy"),date_loan__lt = data.get("date_loan"),data_end__gt =data.get("date_loan"))
        if len(_loans) > 0:
            raise serializers.ValidationError("Copia no disponible")
        
        return super().is_valid(raise_exception=raise_exception)
