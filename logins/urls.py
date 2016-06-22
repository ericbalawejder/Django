from django.conf.urls import url
 
from . import views   # or: from logins import views
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^by_ip/$', views.by_ip, name='by_ip'),
    url(r'^(?P<fail_id>\d+)/$', views.details),
    url(r'^by_login/$', views.by_login, name='by_login'),
]
 
