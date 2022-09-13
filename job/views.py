from job.models import Category
from django.shortcuts import render

def index(request):
    areas = Category.objects.all()

    context = {
        'areas': areas
    }
    return render(request, 'job/index.html', context)
