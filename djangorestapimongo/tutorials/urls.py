from django.conf.urls import url
from tutorials import views

urlpatterns = [
    url(r'^api/getAllAvailableTutorials$', views.getAllAvailableTutorials),
    url(r'^api/newTutorial$', views.newTutorial),
    url(r'^api/getTutorialDetailsById/(?P<id>[0-9]+)$',
        views.getTutorialDetailsById),
    url(r'^api/getTutorialDetailsByName$',
        views.getTutorialDetailsByName),
    # url(r'^api/tutorials$', views.tutorial_list),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
