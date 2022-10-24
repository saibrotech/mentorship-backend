""" ."""

from rest_framework import viewsets

from api.serializers import JobSerializer
from job.models import Job


class PublicJobViewSet(viewsets.ModelViewSet):
    """ ."""

    queryset = Job.objects.all()
    serializer_class = JobSerializer
