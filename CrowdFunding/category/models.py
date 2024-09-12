from django.db import models
from project.models import *
# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    details = models.TextField(blank=False)
    project = models.ForeignKey('project.Project',on_delete=models.CASCADE)