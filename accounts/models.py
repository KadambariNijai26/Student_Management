from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    # ✅ IMPORTANT: use string reference instead of import
    course = models.ForeignKey(
        'students.Course',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    phone = models.CharField(max_length=15, blank=True, default='')
    address = models.TextField(blank=True, default='')
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username