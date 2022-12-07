"""Views for api App."""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.serializers import JobSerializer
from job.models import Job

PARAM_AREA = 'area'
PARAM_SEARCH = 'search'


class PublicJobViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """Public view for Job (without autentication)."""

    serializer_class = JobSerializer

    def get_queryset(self):
        """
        Return the jobs according to search term or by area.

        Returns:
            A job list
        """
        request = self.request

        if PARAM_SEARCH in request.GET:
            search = request.GET.get(PARAM_SEARCH)
            jobs = Job.objects.filter(title__icontains=search)
        elif PARAM_AREA in request.GET:
            area = request.GET.get(PARAM_AREA)
            jobs = Job.objects.filter(category__code=area)
        else:
            jobs = Job.objects.all()

        return jobs
