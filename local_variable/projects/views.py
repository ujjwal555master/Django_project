from .models import ProjectIdeas
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def project_list(request):
    project = ProjectIdeas.objects.all().order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': project})

@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ProjectIdeas.objects.create(
            title=title, 
            description=description, 
            created_by=request.user, 
        )
        return redirect('project_list')
    return render(request, 'projects/create_project.html')


@login_required
def delete_project(request, paper_id):
    project = get_object_or_404(ProjectIdeas, id=paper_id)
    if request.user == project.created_by:
        project.delete()
    return redirect('project_list')