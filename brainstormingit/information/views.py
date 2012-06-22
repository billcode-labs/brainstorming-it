# coding: utf-8

from django.shortcuts import render

from .models import Project

from django import http
from django.views.generic.list import ListView

class ProjectsListView(ListView):
    model = Project
    template_name='information/projects.html'
