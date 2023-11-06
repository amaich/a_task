from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.TaskCreate.as_view(), name='task_create')
]
