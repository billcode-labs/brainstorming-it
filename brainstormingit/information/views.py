# coding: utf-8

from django.shortcuts import render, get_object_or_404 
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms.widgets import HiddenInput

from django import http
from django import forms
from django.views.generic.list import ListView
from django.template import RequestContext

from .models import Project, Solution, Problem, Requirement, Attachment

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
        form = RequirementForm(instance=new_requirement)
        form.fields['vote'].widget = HiddenInput()
        
    else:    
        form = RequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/' + str(id_project))
            
    payload = {'form':form, 'id_project': id_project }
    return render(request, 'information/register_requirement.html', payload)

def edit_requirement(request, id_requirement):
    requirement = get_object_or_404(Requirement, pk=id_requirement)
    id_project = requirement.problem.project.id
    
    if request.POST:
        form = RequirementForm(request.POST, instance=requirement)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/' + str(id_project))
    else:
        form = RequirementForm(instance=requirement)
        form.fields['vote'].widget = HiddenInput()
            
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
        form.fields['like'].widget = HiddenInput()
        form.fields['unlike'].widget = HiddenInput()
        
    else:    
        form = SolutionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/' + str(id_project))
            
    payload = {'form':form, 'id_project': id_project }
    return render(request, 'information/register_solution.html', payload) 

def edit_solution(request, id_solution):
    solution = get_object_or_404(Solution, pk=id_solution)
    id_project = solution.problem.project.id
    
    if request.POST:
        form = SolutionForm(request.POST, instance=solution)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/' + str(id_project))
    else:
        form = SolutionForm(instance=solution)
        form.fields['like'].widget = HiddenInput()
        form.fields['unlike'].widget = HiddenInput()
            
    payload = {'form':form, 'id_project': id_project }
    return render(request, 'information/register_solution.html', payload) 

 

def register_attachment(request, id_solution):
    solution = get_object_or_404(Solution, pk=id_solution)
    
    if request.POST:
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/' + str(solution.problem.project.id))
    else:
        new_attachment = Attachment(solution=solution)
        form = AttachmentForm(instance=new_attachment)
            
    payload = {'form':form, 'id_project': solution.problem.project.id }
    return render(request, 'information/register_attachment.html', payload) 
 
 
class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        
class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
            
            
def problem_more_priority(request, id_problem):
    problem = get_object_or_404(Problem, pk=id_problem)
    problem.vote += 1
    problem.save()
    return project_detail(request, problem.project.id)

def problem_less_priority(request, id_problem):
    problem = get_object_or_404(Problem, pk=id_problem)
    if problem.vote > 0:
        problem.vote -= 1
        problem.save()
    return project_detail(request, problem.project.id)

def requirement_more_priority(request, id_requirement):
    requirement = get_object_or_404(Requirement, pk=id_requirement)
    requirement.vote += 1
    requirement.save()
    return project_detail(request, requirement.problem.project.id)

def requirement_less_priority(request, id_requirement):
    requirement = get_object_or_404(Requirement, pk=id_requirement)
    if requirement.vote > 0:
        requirement.vote -= 1
        requirement.save()
    return project_detail(request, requirement.problem.project.id)

def solution_like(request, id_solution):
    solution = get_object_or_404(Solution, pk=id_solution)
    solution.like += 1
    solution.save()
    return project_detail(request, solution.problem.project.id)
    
def solution_unlike(request, id_solution):
    solution = get_object_or_404(Solution, pk=id_solution)
    solution.unlike += 1
    solution.save()
    return project_detail(request, solution.problem.project.id)
    

def edit_problem(request, id_problem):
    problem = get_object_or_404(Problem, pk=id_problem)
    id_project = problem.project.id
    
    if request.POST:
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/' + str(id_project))
    else:
        form = ProblemForm(instance=problem)
        form.fields['vote'].widget = HiddenInput()
            
    payload = {'form':form, 'id_project': id_project }
    return render(request, 'information/register_problem.html', payload) 


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem