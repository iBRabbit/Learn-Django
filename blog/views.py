from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {
        'title': 'Home',
        'welcome_msg' : 'Welcome to my blog',
    })

def recent_post(request):
    return HttpResponse("This is the recent post page.")