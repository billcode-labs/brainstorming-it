from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brainstormingit.views.home', name='home'),
    # url(r'^brainstormingit/', include('brainstormingit.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #configuracao para ser possivel acessar os arquivos em /media/
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

)

urlpatterns += patterns('',
    url(r'', include('information.urls')),
)
