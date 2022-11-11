"""Views for job App."""

from django.shortcuts import render

from job.models import Category, Job

PARAM_AREA = 'area'


def index(request):
    """
    Home of job App.

    Args:
        request: HTTP request

    Returns:
        HTML
    """
    area = ''
    areas = Category.objects.all()

    if 'search' in request.GET:
        search = request.GET.get('search')
        jobs = Job.objects.filter(title__icontains=search)
    elif PARAM_AREA in request.GET:
        area = request.GET.get(PARAM_AREA)
        jobs = Job.objects.filter(category__code=area)
    else:
        jobs = Job.objects.all()

    context = {
        'areas': areas,
        'jobs': jobs,
        'chosen_area': area,
    }
    return render(request, 'job/index.html', context)


def job_detail(request, pk):
    """
    Job detail page.

    Args:
        request: HTTP request
        pk (int): Job id

    Returns:
        HTML
    """
    job = Job.objects.get(pk=pk)
    context = {
        'job': job,
    }
    return render(request, 'job/job_detail.html', context)


def job_newsletter(request):
    """
    Job newsletter page.

    Args:
        request: HTTP request

    Returns:
        HTML
    """
    email = request.GET.get('email')
    area = request.GET.get(PARAM_AREA)
    areas = Category.objects.all()
    context = {
        'email': email,
        PARAM_AREA: area,
        'areas': areas,
    }
    return render(request, 'job/job_newsletter.html', context)
