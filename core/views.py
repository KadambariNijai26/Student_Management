from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Contact

from students.models import Student
from attendance.models import Attendance
from marks.models import Marks
from fees.models import Fees


# HOME PAGE

def home(request):
    return render(request, 'home.html')


# ABOUT PAGE

def about(request):
    return render(request, 'about.html')


# CONTACT PAGE

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


# TEACHER DASHBOARD

@login_required(login_url='/accounts/login/')
def teacher_dashboard(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'accounts/teacher_dashboard.html', context)


# STUDENT LIST PAGE

@login_required(login_url='/accounts/login/')
def student_list(request):

    students = Student.objects.all()

    course_students = {}

    for student in students:

        if student.course not in course_students:
            course_students[student.course] = []

        course_students[student.course].append(student)

    return render(request, 'accounts/student_list.html', {

        'course_students': course_students

    })


# STUDENT DASHBOARD

@login_required(login_url='/accounts/login/')
def student_dashboard(request):

    student = Student.objects.get(user=request.user)

    attendance = Attendance.objects.filter(student=student)

    marks = Marks.objects.filter(student=student)

    fees = Fees.objects.filter(student=student)

    return render(request, 'accounts/student_dashboard.html', {

        'student': student,
        'attendance': attendance,
        'marks': marks,
        'fees': fees

    })