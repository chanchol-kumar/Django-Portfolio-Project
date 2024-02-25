from django.urls import path
from projects.views import projects,add_projects

urlpatterns = [
    path('',projects, name = 'projects'),
    path('add_projects/',add_projects, name = 'add_projects'),
] 

