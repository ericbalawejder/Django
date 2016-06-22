from django.conf.urls import url
 
from . import views   # or: from logins import views
 
urlpatterns = [
    url(r'^$', views.index),
    
    url(r'^by_ip/$', views.by_ip),
    url(r'^by_login/$', views.by_login),
]
 
