from courseapp.models import Courses
from rest_framework import serializers


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ['cname', 'cimg', 'cauthor', 'cprice']
    
    # Create and return new course instance for valid data
    def create(self, validated_data):
        return Courses.objects.create(**validated_data)
        
    # Update existing data 
    def update(self, instance, validated_data):
        instance.cname = validated_data.get('cname', instance.cname)
        instance.cimg = validated_data.get('cimg', instance.cimg)
        instance.cauthor = validated_data.get('cauthor', instance.cauthor)
        instance.cprice = validated_data.get('cprice', instance.cprice)
        instance.save()
        return instance

    



