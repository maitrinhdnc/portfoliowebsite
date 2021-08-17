from django.shortcuts import render

# Create your views here.
from .models import *

def homePage(request):
    projects = Project.objects.all()
    detailSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')

    context = {'projects': projects, 'skills': skills, 'detailSkills': detailSkills}
    return render(request, 'base/home.html', context)

def project(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'base/project.html', context)