from django.urls import path
from blog.views import blog,add_blog

urlpatterns = [
    path('',blog, name = 'blog'),
    path('add_blog/',add_blog, name = 'add_blog'),
] 
