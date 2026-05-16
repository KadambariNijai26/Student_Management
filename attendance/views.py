from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from accounts.decorators import allowed_users
from students.models import Student
from .models import Attendance


# -------------------------
# Attendance List (All Students)
# -------------------------
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def attendance_students(request):
    students = Student.objects.all()
    return render(request, 'attendance/students.html', {
        'students': students
    })


# -------------------------
# Single Student Attendance
# -------------------------
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def student_attendance(request, id):
    student = get_object_or_404(Student, id=id)
    records = Attendance.objects.filter(student=student)

    total = records.count()
    present = records.filter(status='Present').count()

    percentage = (present / total) * 100 if total > 0 else 0

    return render(request, 'attendance/detail.html', {
        'student': student,
        'records': records,
        'percentage': percentage
    })


# -------------------------
# Add Attendance
# -------------------------
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def add_attendance(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        status = request.POST.get("status")
        date_value = request.POST.get("date")

        if not date_value:
            date_value = date.today()

        Attendance.objects.create(
            student=student,
            status=status,
            date=date_value
        )

        messages.success(request, "Attendance added successfully!")
        return redirect('attendance_students')

    return render(request, 'attendance/add_attendance.html', {
        'student': student
    })


# -------------------------
# Update Attendance
# -------------------------
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def update_attendance(request, id):
    attendance = get_object_or_404(Attendance, id=id)

    if request.method == "POST":
        attendance.status = request.POST.get('status')
        attendance.save()
        return redirect('student_attendance', id=attendance.student.id)

    return render(request, 'attendance/update_attendance.html', {
        'attendance': attendance
    })


# -------------------------
# Delete Attendance
# -------------------------
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def delete_attendance(request, id):
    _ = request
    attendance = get_object_or_404(Attendance, id=id)
    student_id = attendance.student.id
    attendance.delete()

    return redirect('student_attendance', id=student_id)