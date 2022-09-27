from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from api.views import JobViewSet

router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
