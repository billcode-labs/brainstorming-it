# coding: utf-8

from django.shortcuts import render, get_object_or_404 
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django import http
from django import forms
from django.views.generic.list import ListView
from django.template import RequestContext

from .models import Project, Solution, Problem, Requirement

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


def register_requirement(request, id_project):
    problem_id = request.POST.get('problem_id_input', None)
    requirement_name = request.POST.get('requirement_name_input', None)
    
    if problem_id and requirement_name:
        project = get_object_or_404(Project, pk=id_project)
        problem = get_object_or_404(Problem, pk=problem_id)
    
        new_requirement = Requirement(problem=problem, name=requirement_name)
        print 'new requirement:', new_requirement
        form = RequirementForm(instance=new_requirement)
        
    else:    
        form = RequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/' + str(id_project))
            
    payload = {'form':form, 'id_project': id_project }
    return render(request, 'information/register_requirement.html', payload)

class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement


def register_solution(request, id_project):
    problem_id = request.POST.get('problem_id_input', None)
    solution_name = request.POST.get('solution_name_input', None)
    
    if problem_id and solution_name:
        project = get_object_or_404(Project, pk=id_project)
        problem = get_object_or_404(Problem, pk=problem_id)
    
        new_solution = Solution(problem=problem, name=solution_name)
        form = SolutionForm(instance=new_solution)
        
    else:    
        form = SolutionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/' + str(id_project))
            
    payload = {'form':form, 'id_project': id_project }
    return render(request, 'information/register_solution.html', payload) 
 
class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
            