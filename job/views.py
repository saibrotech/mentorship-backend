from unicodedata import category
from job.models import Category, Job
from django.shortcuts import render


def index(request):
    areas = Category.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        jobs = Job.objects.filter(title__icontains=search)
    elif 'area' in request.GET:
        area = request.GET['area']
        jobs = Job.objects.filter(category__code=area)
    else:
        jobs = Job.objects.all()

    context = {
        'areas': areas,
        'jobs': jobs
    }
    return render(request, 'job/index.html', context)
