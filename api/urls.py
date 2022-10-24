from django.urls import include, path
from rest_framework import routers

from api.views import PublicJobViewSet

router = routers.DefaultRouter()
router.register(r'public/jobs', PublicJobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
