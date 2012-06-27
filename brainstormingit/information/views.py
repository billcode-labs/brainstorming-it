# coding: utf-8

from django.shortcuts import render, get_object_or_404 
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django import http
from django import forms
from django.views.generic.list import ListView
from django.template import RequestContext

from .models import Project, Solution, Problem

class ProjectsListView(ListView):
    model = Project
    template_name='information/project_list.html'


def project_detail(request, id_project):
    project = get_object_or_404(Project, pk=id_project)
    return render(request, 'information/project_detail.html', {'project': project, 'id_project': id_project})

def solution_detail(request, id):
    solution = get_object_or_404(Solution, pk=id)
    return render(request, 'information/solution_detail.html', {'solution': solution})


def register_problem(request, id_project):
    project = get_object_or_404(Project, pk=id_project)
    problem_name = request.POST['problem_name_input']
    print problem_name
    new_problem = Problem(project=project, name=problem_name)
    new_problem.save()
    return HttpResponseRedirect('/projects/' + str(id_project))


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem    