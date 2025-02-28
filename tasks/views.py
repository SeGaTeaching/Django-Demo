from django.shortcuts import render
from django.http import JsonResponse
from .models import TaskForm
from .forms import TaskFormular

# Create your views here.
def tasks_list(request):
    tasks = TaskForm.objects.all().order_by('-created_at')
    form = TaskFormular()
    
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks, 'form': form})


def add_task(request):
    if request.method == "POST":
        form = TaskFormular(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            task = TaskForm.objects.create(title=title)
            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'created_at': task.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
    return JsonResponse({'error': 'Invalid request'}, status=400)
