from django.urls import path
from .views import *
urlpatterns = [
    path('', apiOverview, name='api-over-view'),
    path('list-view/', listView, name='list-view'),
    path('task-details/<int:id>/', taskView, name='task-details'),
    path('create-task/', createTask, name='create-task'),
    path('update-task/<int:id>/', updateTask, name='update-task'),
    path('delete-task/<int:id>/', deleteTask, name='dalete-task'),
]