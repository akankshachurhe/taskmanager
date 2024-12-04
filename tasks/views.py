from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.utils import timezone


#Home view (lists task)
@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/home.html', {'tasks': tasks})


#create task view

@login_required
def create_task(request):
    if request.method == 'POST':
        tittle = request.POST.get('tittle')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')

        Task.objects.create(
            tittle=tittle,
            description=description,
            due_date=due_date,
            priority=priority,
            user=request.user
        )
        return redirect('home')
    return render(request, 'tasks/create_task.html')


# Mark task as complete.
@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('home')
                                    
                                    
                                    
  
def login(request):
    return render(request, 'login.html')      