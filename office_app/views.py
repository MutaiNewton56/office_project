from rest_framework import viewsets
from .models import Department, ChickenBatch
from .serializers import DepartmentSerializer, ChickenBatchSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ChickenBatchViewSet(viewsets.ModelViewSet):
    queryset = ChickenBatch.objects.all()
    serializer_class = ChickenBatchSerializer
