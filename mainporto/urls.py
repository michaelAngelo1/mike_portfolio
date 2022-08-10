from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('projects', views.projects, name='projects'),
    path('achievements', views.achievement, name='achievement'),
    path('certifications', views.certifications, name='certifications')
]