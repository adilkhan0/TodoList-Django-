from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from .forms import taskform
# Create your views here.
def home(request):
    tasks=task.objects.all()
    form=taskform()
    if request.method=='POST':
        form=taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'tasks':tasks,'form':form}
    
    return render(request,'home.html',context)
def updatetask(request,pk):
    tasks=task.objects.get(id=pk)
    form=taskform(instance=tasks)
    if request.method=='POST':
        form=taskform(request.POST,instance=tasks)
        if form.is_valid:
            form.save()
            return redirect('/')
    context={'form':form}
    return render (request,'update_task.html',context)
def deletetask(request,pk):
    item=task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    
    context={'item':item}
    return render(request, 'delete.html', context)
