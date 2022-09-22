from unicodedata import category
from job.models import Category, Job
from django.shortcuts import render

def index(request):
    areas = Category.objects.all()
    jobs = Job.objects.all()

    if 'area' in request.GET:
        area = request.GET['area']
        jobs = Job.objects.filter(category__code=area)
    else:
        jobs = Job.objects.all()

    context = {
        'areas': areas,
        'jobs': jobs,
    }
    return render(request, 'job/index.html', context)