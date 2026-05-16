from django.db import models
from accounts.models import UserProfile   # optional if needed

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)

    # ✅ FIXED FK
    course = models.CharField(max_length=100, default='General')

    contact = models.CharField(max_length=15)
    aadhar = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name