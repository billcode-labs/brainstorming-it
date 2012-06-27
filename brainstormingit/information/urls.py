from django.conf.urls import patterns, url

from .views import ProjectsListView, project_detail, solution_detail, register_problem, register_requirement

urlpatterns = patterns('information.views',
    
    url(r'^projects/solution/(\d+)', solution_detail, name='url_solution_detail'),
    
    url(r'^projects/(\d+)', project_detail, name='url_project_detail'),
    
    url(r'^projects', ProjectsListView.as_view(), name='url_project_list'),
    
    url(r'^problem/new/(\d+)', register_problem, name='url_register_problem'),
    
    url(r'^requirement/new/(\d+)', register_requirement, name='url_register_requirement'),
    
)
