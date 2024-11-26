from rest_framework import serializers
from .models import Kpi, KpiAssetLink

class KpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kpi
        fields = ["id","name","expression","description"]


class KpiAssetSerializer(serializers.ModelSerializer):
    class Meta: 
        model = KpiAssetLink
        fields = '__all__'
        