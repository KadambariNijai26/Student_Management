from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

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
