from django.shortcuts import render
from . import models

# Create your views here.
def base(request):
    return render(request, "base.html")

def projects(request):
    projects = models.Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def achievement(request):
    achievements = models.Achievement.objects.all()
    return render(request, "achievements.html", {'achievements': achievements})

def certifications(request):
    return render(request, "certifications.html")