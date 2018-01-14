"""
URLs for app_forum
"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('^$', views.index),    
    re_path(r'^(?P<category>[\w]+)/(?P<postId>[\d]+)$', views.forumPost)    
]