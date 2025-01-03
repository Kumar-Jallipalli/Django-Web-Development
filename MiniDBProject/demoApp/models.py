from django.db import models

# Create your models here.
class employeeTable (models.Model):
    eNo = models.IntegerField()
    eName = models.CharField(max_length=30)
    eSal = models.FloatField()
    eAdd = models.CharField(max_length=30)