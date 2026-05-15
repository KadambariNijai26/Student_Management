from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from students.models import Student
from .models import Marks


# -------------------------
# Student List (Marks Module)
# -------------------------
@login_required(login_url='/accounts/login/')
def marks_students(request):
    students = Student.objects.all()
    return render(request, 'marks/students.html', {
        'students': students
    })


# -------------------------
# Student-wise Marks View
# -------------------------
@login_required(login_url='/accounts/login/')
def student_marks(request, id):
    student = get_object_or_404(Student, id=id)
    records = Marks.objects.filter(student=student)

    return render(request, 'marks/detail.html', {
        'student': student,
        'records': records
    })


# -------------------------
# Add Marks
# -------------------------
@login_required(login_url='/accounts/login/')
def add_marks(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        Marks.objects.create(
            student=student,
            subject=request.POST.get('subject'),
            marks=request.POST.get('marks')
        )

        messages.success(request, "Marks added successfully!")
        return redirect('marks_students')

    return render(request, 'marks/add_marks.html', {
        'student': student
    })


# -------------------------
# Update Marks
# -------------------------
@login_required(login_url='/accounts/login/')
def update_marks(request, id):
    marks = get_object_or_404(Marks, id=id)

    if request.method == "POST":
        marks.subject = request.POST.get('subject')
        marks.marks = request.POST.get('marks')
        marks.save()

        return redirect('student_marks', id=marks.student.id)

    return render(request, 'marks/update_marks.html', {
        'marks': marks
    })


# -------------------------
# Delete Marks
# -------------------------
@login_required(login_url='/accounts/login/')
def delete_marks(request, id):
    marks = get_object_or_404(Marks, id=id)
    student_id = marks.student.id
    marks.delete()

    return redirect('student_marks', id=student_id)