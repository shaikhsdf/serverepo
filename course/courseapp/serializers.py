#sdf
from courseapp.models import Courses
from rest_framework import serializers

#sdf
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ['cname', 'cimg', 'cauthor', 'cprice']
   

    



