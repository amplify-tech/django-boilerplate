from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    grade = models.IntegerField()
    enrolled_date = models.DateField(auto_now_add=True)
