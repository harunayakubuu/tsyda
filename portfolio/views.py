from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectCreateForm, ProjectUpdateForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


# Frontend
def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'frontend/portfolio/project_list.html', context)

def project_detail(request, id):
    project = Project.objects.get(id = id)
    context = {
        'project': project
    }
    return render(request, 'frontend/portfolio/project_detail.html', context)


# Backend
def portfolios(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'backend/portfolio/projects.html', context)


def portfolio_detail(request, id):
    project = Project.objects.get(id = id)
    context = {
        'project': project
    }
    return render(request, 'backend/portfolio/project_detail.html', context)


def project_create(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            form.save()
            return redirect('/portfolio/project/list/')
    else:
        form = ProjectCreateForm()
    context = {
        'form': form
    }
    return render(request, 'backend/portfolio/project_add.html', context)

def portfolio_update(request, id):
    instance = get_object_or_404(Project, id=id)
    form = ProjectUpdateForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/portfolio/project/list/')
    
    context = {
        'instance': instance,
        'form': form
    }
    return render(request, 'backend/portfolio/project_update.html', context)

class portfolio_delete(DeleteView):
    model = Project
    template_name = 'backend/portfolio/project_delete.html'
    success_url = reverse_lazy('portfolio-list')