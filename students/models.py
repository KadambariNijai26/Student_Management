from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    aadhar = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
# Create your models here.
