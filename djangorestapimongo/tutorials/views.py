from django.shortcuts import render
# Create your views here.
from django.http.response import HttpResponse, JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer


# Get All the available tutorials
@api_view(['GET'])
def getAllAvailableTutorials(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorial_Serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorial_Serializer.data, safe=False)


# Create a new tutorial
@api_view(['POST'])
def newTutorial(request):
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse('Error', status=status.HTTP_400_BAD_REQUEST)


# Get tutorial details by id
@api_view(['GET'])
def getTutorialDetailsById(request, id):
    if request.method == 'GET':
        tutorial = Tutorial.objects.get(id=id)
        tutorial_serializer = TutorialSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data, status=status.HTTP_200_OK)
    return JsonResponse('Error', status=status.HTTP_400_BAD_REQUEST)


# Get tutorial details by title
@api_view(['GET'])
def getTutorialDetailsByName(request):
    if request.method == 'GET':
        tutorial = Tutorial.objects.all()
        title = request.GET.get('title', None)
        tutorial = tutorial.filter(title__icontains=title)
        tutorial_serializer = TutorialSerializer(tutorial, many=True)
        return JsonResponse(tutorial_serializer.data, safe=False, status=status.HTTP_200_OK)
    return JsonResponse('Error', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    """ Retrieve objects (with condition)
        Retrieve all Tutorials/ find by title from MongoDB database
    """
    if request.method == 'GET':
        tutorial = Tutorial.objects.all()
        title = request.GET.get('title', None)
    pass


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, id):
    try:
        tutorial = Tutorial.objects.get(pk=id)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def tutorial_list_published(request):
    pass
