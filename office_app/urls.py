from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, ChickenBatchViewSet  # import your viewsets

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'chickens', ChickenBatchViewSet)
# add more as needed...

urlpatterns = [
    path('', include(router.urls)),
]
