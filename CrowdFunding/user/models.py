from django.db import models
from project.models import *
# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20,blank=False)
    lname = models.CharField(max_length=20,blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=20,blank=False)
    phone = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='user/images', blank=False, null=True)
    birth_date = models.DateField()
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE)


