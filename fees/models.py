from django.db import models
from students.models import Student

class Fees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_fees = models.IntegerField()
    paid_fees = models.IntegerField()

    @property
    def remaining_fees(self):
        return self.total_fees - self.paid_fees
    def __str__(self):
        return self.student.name
# Create your models here.
