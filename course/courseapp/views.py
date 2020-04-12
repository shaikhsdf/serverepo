from django.shortcuts import render
from django.http import HttpResponse, Http404 
from courseapp.storecourse import newCourse
#from django.models import Courses
from courseapp.models import Courses
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from rest_framework import permissions
from courseapp.serializers import CourseSerializer
#from course.courseapp.serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [permissions.IsAuthenticated]

def index(request):
    return HttpResponse("Hello.")

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