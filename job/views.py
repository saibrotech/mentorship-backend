from job.models import Category, Job
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

def index(request):
    areas = Category.objects.all()
    jobs = Job.objects.all()
    filter= [DjangoFilterBackend]
    filterset_fields = ['job']

    context = {
        'areas': areas,
        'jobs': jobs,
        'filter':filter,
        'filterset_fields':filterset_fields,
    }
    return render(request, 'job/index.html', context)