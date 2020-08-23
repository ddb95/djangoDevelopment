from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.homepageSilchar, name='homepage'),
    path('blog', views.blog, name='blog')
]
