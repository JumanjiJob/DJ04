from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='films_home'),
    path('review', views.review, name='films_review'),
    path('create_review', views.create_review, name='films_create_review'),
]