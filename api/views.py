from rest_framework import mixins, viewsets
from api.serializers import JobSerializer
from job.models import Job

class PublicJobViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
