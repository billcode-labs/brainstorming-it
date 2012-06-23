from django.conf.urls import patterns, url

from .views import ProjectsListView, project_detail, solution_detail

urlpatterns = patterns('information.views',
    
    url(r'^projects/solution/(\d+)', solution_detail, name='url_solution_detail'),
    
    url(r'^projects/(\d+)', project_detail, name='url_project_detail'),
    
    url(r'^projects', ProjectsListView.as_view(), name='url_project_list'),
    
)
