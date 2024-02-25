from django.urls import path
from review.views import review,show_review

urlpatterns = [
    path('', review, name='review'),
    path('show_review/', show_review, name='show_review'),
]