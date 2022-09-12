from django.shortcuts import render

def index(request):
    areas = [
        {
            'name': 'Desenvolvimento'
        },
        {
            'name': 'Suporte'
        },
        {
            'name': 'Infraestrutura'
        },
        {
            'name': 'Ciência de Dados'
        }, 
        {
            'name': 'Segurança'
        }, 
        {
            'name': 'Produto'
        }
    ]
    context = {
        'areas': areas
    }
    return render(request, 'job/index.html', context)