from job.models import Category, Job
from django.shortcuts import render


def index(request):
    areas = Category.objects.all()
    area = ''
    categorys = Category.objects.all()

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
        'jobs': jobs,
        'chosen_area': area,
        'categorys': categorys
    }
    return render(request, 'job/index.html', context)

def job_detail(request, id):
    job = Job.objects.get(pk=id)
    context = {
        'job': job
    }
    return render(request, 'job/job_detail.html', context)