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

    if PARAM_AREA in request.GET:
        area = request.GET.get(PARAM_AREA)

    context = {
        'areas': areas,
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
    area_code = request.GET.get(PARAM_AREA)
    areas = Category.objects.all()
    submited = 'action' in request.GET

    context = {
        'email': email,
        'area_code': area_code,
        'areas': areas,
        'submited': submited,
    }
    return render(request, 'job/job_newsletter.html', context)


def job_new(request):
    """
    Return new job page.

    Args:
        request: HTTP request

    Returns:
        HTML
    """
    return render(request, 'job/new-jobs-criteria.html')
