from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def index(request):
    Task = myTask.objects.all()
    form = myTaskForm()
    if request.method == 'POST':
        form = myTaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'Task': Task, 'form': form}
    return render(request, 'TODO_app/list.html', context)

def updateTask(request,pk):
    task = myTask.objects.get(id=pk)
    form = myTaskForm(instance=task)
    if request.method == 'POST':
        form = myTaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'TODO_app/update.html', context)



def delete(request,pk):
    item = myTask.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context={'item': item}

    return render(request,'TODO_app/delete.html', context)
