from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('recent-post', views.recent_post, name='recent_post')
]