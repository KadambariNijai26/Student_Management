from django.db import models
from students.models import Student

class Fees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total = models.IntegerField()
    paid = models.IntegerField()
    due = models.IntegerField()
# Create your models here.
