from django import forms
from courseapp.models import Courses

class newCourse(forms.ModelForm):
    class Meta():
        model = Courses
        fields = '__all__'