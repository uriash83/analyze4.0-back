from rest_framework import serializers
from . import models

class FactorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Factors
        #fields = ('id', 'user','tss','ctl','atl','tbs','date')
        fields = ('__all__')
