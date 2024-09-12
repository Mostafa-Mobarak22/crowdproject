from django.db import models
# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    details = models.TextField(blank=False)
    image = models.ImageField(upload_to='user/images', blank=False, null=True)
    target = models.IntegerField(blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.TextField()

