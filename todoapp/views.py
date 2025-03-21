from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def home_page_view(request):
    return HttpResponse('Hello, World!')

def task_list(request):
    tasks = Task.objects.prefetch_related('subtasks').all()
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})