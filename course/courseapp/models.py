from django.db import models

class Courses(models.Model): 
    cname = models.CharField(max_length=300) 
    cimg = models.ImageField(upload_to='images/') 
    cauthor = models.CharField(max_length=100)
    cprice = models.FloatField()
    def __str__(self):
        return self.cname


