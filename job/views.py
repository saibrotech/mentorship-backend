from job.models import Category, Job
from django.shortcuts import render

def index(request):
    areas = Category.objects.all()
    jobs = Job.objects.all()

    context = {
        'areas': areas,
        'jobs': jobs,
    }
    return render(request, 'job/index.html', context)