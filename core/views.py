from django.shortcuts import render, redirect
from .models import Contact
from students.models import Student
from attendance.models import Attendance
from marks.models import Marks
from fees.models import Fees


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        return redirect('/')

    return render(request, 'contact.html')

def teacher_dashboard(request):
    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'teacher_dashboard.html', context)
# Create your views here.
