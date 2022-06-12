from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField()
    name=models.CharField(max_length=40)
    branch=models.CharField(max_length=40)
    photo=models.ImageField(upload_to='pic', blank=True)
    dmc=models.FileField(upload_to='dmcs', blank=True)

