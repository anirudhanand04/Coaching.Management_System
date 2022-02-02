from django.db import models

# Create your models here.
class Courses(models.Model):
    coursename = models.CharField(max_length=100)
    hours = models.IntegerField()
    months=models.IntegerField()
    modules=models.IntegerField()
    photo=models.ImageField()
    videolink=models.CharField(max_length=255,default=None)

    def __str__(self):
        return self.coursename