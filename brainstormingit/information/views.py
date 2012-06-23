# coding: utf-8

from django.shortcuts import render, get_object_or_404 

from .models import Project, Solution

from django import http
from django.views.generic.list import ListView

class ProjectsListView(ListView):
    model = Project
    template_name='information/project_list.html'


def project_detail(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'information/project_detail.html', {'project': project})

def solution_detail(request, id):
    solution = get_object_or_404(Solution, pk=id)
    return render(request, 'information/solution_detail.html', {'solution': solution})

