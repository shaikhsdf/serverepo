from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse 
from courseapp.storecourse import newCourse
from courseapp.models import Courses
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, status
from rest_framework.response import Response
from courseapp.serializers import CourseSerializer
from rest_framework.decorators import api_view



#api for creating and/or listing courses
@api_view(['GET','POST'])
@csrf_exempt
def course_list(request):

    #code to list all courses
    if request.method == 'GET':
        allcourses = Courses.objects.all()
        serializer = CourseSerializer(allcourses, many = True)
        return Response(serializer.data)
    
    #code to create a new course
    elif request.metod == 'POST':
        #data = JSONParser().parse(request) #comment nd see
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#View to correspond ton each course to update or delete 
@api_view(['GET','PUT', 'DELETE'])
@csrf_exempt
def course_detail(request, pk):
    try:
        eachcourse = Courses.objects.get(pk = pk)
    except Courses.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(eachcourse)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = CourseSerializer(eachcourse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        eachcourse.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

def index(request):
    return HttpResponse("Hello.")
    #return render(request, 'index.html')

@csrf_protect
def storeCourses(request):
    form = newCourse

    if request.method == "POST":
        form = newCourse(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #return index(request)
        else:
            print('Invalid Data')
    
    return render(request, 'courseapp/store.html', {'form': form})

def showCourses(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        courseList = Courses.objects.all()  
        return render(request, 'courseapp/courselist.html', {'courseList':courseList}) 


def detail(request, course_id):
    try:
        course = Courses.objects.get(pk=course_id)
    except Courses.DoesNotExist:
        return HttpResponse("Course does not exist")
    return render(request, 'courseapp/detail.html', {'course': course})