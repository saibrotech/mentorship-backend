from django.shortcuts import render

def index(request):
    context = {
        'text': 'Hello Word!'
    }
    return render(request, 'job/index.html', context)
