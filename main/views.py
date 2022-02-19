from django.shortcuts import render, redirect
from main.models import Task

def index(request):
    task_list = Task.objects.all()
    return render(request, 'main/index.html', {'task_list': list(task_list)})


def add(request):
    title = request.POST.get('task_input')
    complete = request.POST.get('completed_input')
    if complete == 'on':
        complete = True
    else:
        complete = False
    task = Task(title=title, complete=complete)
    task.save()
    return redirect('/')


def delete(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('/')


def complete(request,task_id):
    task = Task.objects.get(pk=task_id)

    if task.complete == False:
        task.complete = True
    else:
        task.complete = False

    task.save()
    return redirect('/')