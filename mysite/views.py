from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'contributors': ['John', 'Jane', 'Joe']
    }
    return render(request, 'index.html', context=context)

def about(request):
    return HttpResponse("This is the about page.")