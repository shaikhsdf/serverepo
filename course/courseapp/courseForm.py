from courseapp.models import Courses
from django.forms import ModelForm

class courseForm(ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'