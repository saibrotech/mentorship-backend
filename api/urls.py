from django.urls import path, include
from rest_framework import routers

from api.views import PublicJobViewSet

router = routers.DefaultRouter()
router.register(r'public/jobs', PublicJobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
