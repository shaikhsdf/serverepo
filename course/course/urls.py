"""course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#sdf
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
#sdf
from courseapp import views
from rest_framework import routers

#sdf
router = routers.DefaultRouter()
router.register(r'mycourse', views.CourseViewSet)

urlpatterns = [
    #sdf
    path('', include(router.urls)),   
    #path('', views.index, name='index'),    
]

#urlpatterns = format_suffix_patterns(urlpatterns)
#sdf
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)