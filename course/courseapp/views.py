from django.shortcuts import render
from django.http import HttpResponse, Http404 
from courseapp.storecourse import newCourse
from courseapp.models import Courses

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def storeCourses(request):
    form = newCourse

    if request.method == "POST":
        form = newCourse(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(requesr)
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