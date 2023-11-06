from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .models import Task
from .forms import TaskForm


# Create your views here.
class TaskCreate(View):
    def get(self, request):
        form = TaskForm
        return render(request, 'tasks/task_create.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return HttpResponseRedirect('/tasks')


def index(request):
    return render(request, 'tasks/index.html')
