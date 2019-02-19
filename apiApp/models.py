from django.db import models

# Create your models here.


class ProjectCat(models.Model):
    ProjectId = models.IntegerField()
    CarId = models.IntegerField()
    CartName = models.CharField(max_length=225)

class ApiName(models.Model):
    ProjectId = models.IntegerField()
    CarId = models.IntegerField()
    ApiId = models.IntegerField()
    ApiName = models.CharField(max_length=225)