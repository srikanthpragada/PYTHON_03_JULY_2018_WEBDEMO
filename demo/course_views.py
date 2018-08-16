from django.shortcuts import render, redirect
import sqlite3
from .models import Course
from .course_forms import CourseForm


def list(request):
    return render(request, 'course/list.html', {'courses': Course.objects.all()})


def add(request):
    message = ""
    if request.method == "POST":
        f = CourseForm(request.POST)
        if f.is_valid():
           f.save()
           message  = "Course has been added!"
        else:
           message = "Invalid data!"
    else:
        f = CourseForm()

    return render(request, 'course/add.html', {'form': f, 'message' : message})
