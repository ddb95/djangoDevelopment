from django.shortcuts import render, get_object_or_404
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
        try:
            tutorial = get_object_or_404(Tutorial, pk=id)
            tutorial_serializer = TutorialSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_200_OK)
        except Tutorial.DoesNotExist:
            return JsonResponse('Error', status=status.HTTP_400_BAD_REQUEST)
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


# Update an object by id
@api_view(['POST'])
def updateExistingObject(request, id):
    tutorial = Tutorial.objects.get(id=id)
    tutorial_data = JSONParser().parse(request)
    tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
    if tutorial_serializer.is_valid():
        tutorial_serializer.save()
        return JsonResponse(tutorial_serializer.data, safe=False, status=status.HTTP_200_OK)
    return JsonResponse(tutorial_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)


# Delete an existing object
@api_view(['DELETE'])
def deleteExistingObject(request, id):
    tutorial = Tutorial.objects.get(id=id)
    tutorial.delete()
    return JsonResponse({'Message: Tutorial was deleted successfully'}, safe=False, status=status.HTTP_200_OK)
