from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('code', 'title', 'duration', 'fee')


@api_view(['GET','POST'])
def list_courses(request):
    if request.method == "GET":
       courses = Course.objects.all()
       serializer = CourseSerializer(courses, many=True)
       return Response(serializer.data)
    else:  # Post
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Successful post

        return Response(serializer.errors, status=400)  #Invalid data



@api_view(['GET','DELETE','PUT'])
def course_details(request, code):
    try:
        course = Course.objects.get(code=code)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    elif request.method == 'PUT':    # Update
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
           serializer.save()    # Update table in DB
           return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=204)
