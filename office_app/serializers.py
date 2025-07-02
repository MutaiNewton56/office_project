from rest_framework import serializers
from .models import Department, ChickenBatch

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ChickenBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChickenBatch
        fields = '__all__'
