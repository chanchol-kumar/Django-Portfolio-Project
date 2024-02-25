from django.urls import path
from skill.views import skill,add_skill

urlpatterns = [
    path('',skill, name = 'skill'),
    path('add_skill/',add_skill, name = 'add_skill'),
] 
