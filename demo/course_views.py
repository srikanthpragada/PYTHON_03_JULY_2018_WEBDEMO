from django.shortcuts import render, redirect
import json
from .models import Course
from .course_forms import CourseForm
from django.http import JsonResponse, HttpResponse


def list(request):
    return render(request, 'course/list.html', {'courses': Course.objects.all()})


def add(request):
    message = ""
    if request.method == "POST":
        f = CourseForm(request.POST)
        if f.is_valid():
            f.save()
            message = "Course has been added!"
        else:
            message = "Invalid data!"
    else:
        f = CourseForm()

    return render(request, 'course/add.html', {'form': f, 'message': message})


def search(request):
    return render(request, 'course/search.html')


def search_courses(request):
    title = request.GET["title"];
    courses = Course.objects.filter(title__contains=title)
    cl = []
    for c in courses:
        cl.append({'code': c.code, 'title': c.title, 'fee': c.fee, 'duration': c.duration})

    return HttpResponse(json.dumps(cl))
