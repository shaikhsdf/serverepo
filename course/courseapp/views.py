from courseapp.models import Courses
from rest_framework import viewsets, status
from courseapp.serializers import CourseSerializer
from django.http import Http404
from django.shortcuts import render

#sdf
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

#View to display all courses in a web page
def courseview(request):
    try:
        courselist = Courses.objects.all()
    except Courses.DoesNotEcist:
        raise Http404("No Courses exist")
    return render(request, 'courseapp/coursepage.html', {'courselist': courselist})

