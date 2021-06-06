from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('experience', views.experience, name = 'experience'),
    path('education', views.education, name = 'education'),
    path('skills', views.skills, name = 'skills'),
    path('interests', views.interests, name = 'interests'),
    path('awards', views.awards, name = 'awards'),

]