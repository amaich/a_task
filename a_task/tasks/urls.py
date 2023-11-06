from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.TaskCreate.as_view(), name='task_create')
]
