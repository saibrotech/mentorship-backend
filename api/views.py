"""Views for api App."""

from rest_framework import viewsets

from api.serializers import JobSerializer
from job.models import Job


class PublicJobViewSet(viewsets.ModelViewSet):
    """Public view for Job (without autentication)."""

    queryset = Job.objects.all()
    serializer_class = JobSerializer
