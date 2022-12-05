"""URLs for api App."""

from django.urls import include, path
from rest_framework import routers

from api.views import PublicJobViewSet

router = routers.DefaultRouter()
router.register('public/jobs', PublicJobViewSet, basename='job')

urlpatterns = [
    path('', include(router.urls)),
]
