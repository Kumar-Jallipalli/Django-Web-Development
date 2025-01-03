from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.IntegerField()
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField()
    phone_no = models.BigIntegerField()
    address = models.TextField()