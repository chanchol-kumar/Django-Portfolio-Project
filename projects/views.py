from django.shortcuts import render,redirect
from projects.models import ProjectsModel
from projects.forms import ProjectsForm

def add_projects(request):
    form = ProjectsForm()
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectsForm()
    return render(request, 'projects/add_projects.html', {'form':form})

def projects(request):
    projects = ProjectsModel.objects.order_by('-timestamp')
    return render(request, 'projects/projects.html', {'projects': projects})

