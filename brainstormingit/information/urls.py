from django.conf.urls import patterns, url

from .views import ProjectsListView, project_detail, solution_detail, register_problem, register_requirement, register_solution, register_attachment
from .views import problem_more_priority, problem_less_priority

urlpatterns = patterns('information.views',
    
    url(r'^projects/solution/(\d+)', solution_detail, name='url_solution_detail'),
    
    url(r'^projects/(\d+)', project_detail, name='url_project_detail'),
    
    url(r'^projects', ProjectsListView.as_view(), name='url_project_list'),
    
    url(r'^problem/new/(\d+)', register_problem, name='url_register_problem'),
    
    url(r'^problem/more_priority/(\d+)', problem_more_priority, name='url_problem_more_priority'),
    
    url(r'^problem/less_priority/(\d+)', problem_less_priority, name='url_problem_less_priority'),
    
    url(r'^requirement/new/(\d+)', register_requirement, name='url_register_requirement'),
    
    url(r'^solution/new/(\d+)', register_solution, name='url_register_solution'),
    
    url(r'^attachment/new/(\d+)', register_attachment, name='url_register_attachment'),
    
)
