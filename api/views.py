from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tasks
from .serializers import taskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    urls = {
        'view full tasks list':'list-view/',
        'details of a task':'task-details/<int:id>/',
        'create a new task': 'create-task/',
        'update a task':'update-task/<int:id>/',
        'delete a task':'delete-task/<int:id>/',
    }
    return Response(urls)

@api_view(['GET'])
def listView(request):
    all_tasks = Tasks.objects.all().order_by('-id')
    my_serializer = taskSerializer(all_tasks, many=True)
    
    return Response(my_serializer.data)

@api_view(['GET'])
def taskView(request, id):
    my_task = Tasks.objects.get(id=id)
    my_serializer = taskSerializer(my_task, many=False)
    return Response(my_serializer.data)

@api_view(['POST'])
def createTask(request):
    newTask = taskSerializer(data=request.data)
    if newTask.is_valid():
        newTask.save()
    return Response(newTask.data)

@api_view(['POST'])
def updateTask(request, id):  # remember to create a custom serializer to prevent id editing
    my_task = Tasks.objects.get(id=id)
    my_serializer = taskSerializer(instance=my_task, data=request.data)
    if my_serializer.is_valid():
        my_serializer.save()
    return Response(my_serializer.data)

@api_view(['DELETE'])
def deleteTask(request, id):
    my_task = Tasks.objects.get(id=id)
    my_task.delete()
    return Response('item successfully deleted')
