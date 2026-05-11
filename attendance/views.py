from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Attendance


@login_required(login_url='/login/')
def attendance_view(request):

    records = Attendance.objects.all()

    total = records.count()

    present = records.filter(status='Present').count()

    percentage = 0

    if total > 0:

        percentage = (present / total) * 100

    return render(request, 'attendance.html', {

        'records': records,

        'percentage': percentage

    })
# Create your views here.
