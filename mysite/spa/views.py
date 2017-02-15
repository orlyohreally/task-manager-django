from django.shortcuts import render, get_object_or_404, Http404,  redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
def index(request):
	context = {
		'tasks': Task.objects.all()
	}
	return render(request, 'spa/index.html', context)

def newTask(request):
	if (request.is_ajax()):
		if (request.method == 'POST'):
			if(request.POST.get('Task') != ""):
				pr = request.POST.get('main')
				if(pr):
					main = get_object_or_404(Task, pk = pr)
					instance = Task(task_text = request.POST.get('Task'), main_task = main)
				else:
					instance = Task(task_text = request.POST.get('Task'))
					
				instance.save()
				return HttpResponse(instance.pk);
	return redirect('spa:index')
def deleteTask(request):
	if (request.is_ajax()):
		if (request.method == 'POST'):
			instance = get_object_or_404(Task, pk = request.POST.get('pk'))
			instance.delete()
	return redirect('spa:index')
def updateTask(request):
	if (request.is_ajax()):
		if (request.method == 'POST'):
			instance = get_object_or_404(Task, pk = request.POST.get('pk'))
			instance.task_text = request.POST.get('newText')
			instance.save()
	return redirect('spa:index')