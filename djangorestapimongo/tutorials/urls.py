from django.conf.urls import url
from tutorials import views

urlpatterns = [
    url(r'^api/getAllAvailableTutorials$', views.getAllAvailableTutorials),
    url(r'^api/newTutorial$', views.newTutorial),
    url(r'^api/getTutorialDetailsById/(?P<id>[0-9]+)$',
        views.getTutorialDetailsById),
    url(r'^api/updateExistingObject/(?P<id>[0-9]+)$',
        views.updateExistingObject),
    url(r'^api/getTutorialDetailsByName$',
        views.getTutorialDetailsByName),
    url(r'^api/deleteExistingObject/(?P<id>[0-9]+)$',
        views.deleteExistingObject),
]
