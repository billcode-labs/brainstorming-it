from django.conf.urls import patterns, url

from .views import ProjectsListView

urlpatterns = patterns('information.views',
    
    url(r'^projects', ProjectsListView.as_view()),
    
)
