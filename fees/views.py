from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from students.models import Student
from .models import Fees


# -------------------------
# Student List (Fees Module)
# -------------------------
@login_required(login_url='/accounts/login/')
def fees_students(request):
    students = Student.objects.all()
    return render(request, 'fees/students.html', {
        'students': students
    })


# -------------------------
# Student-wise Fees View
# -------------------------
@login_required(login_url='/accounts/login/')
def student_fees(request, id):
    student = get_object_or_404(Student, id=id)
    records = Fees.objects.filter(student=student)

    return render(request, 'fees/detail.html', {
        'student': student,
        'records': records
    })


# -------------------------
# Add Fees
# -------------------------
@login_required(login_url='/accounts/login/')
def add_fees(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        Fees.objects.create(
            student=student,
            total_fees=request.POST.get('total_fees'),
            paid_fees=request.POST.get('paid_fees')
        )

        messages.success(request, "Fees added successfully!")
        return redirect('fees_students')

    return render(request, 'fees/add_fees.html', {
        'student': student
    })


# -------------------------
# Update Fees
# -------------------------
@login_required(login_url='/accounts/login/')
def update_fees(request, id):
    fees = get_object_or_404(Fees, id=id)

    if request.method == "POST":
        fees.total_fees = request.POST.get('total_fees')
        fees.paid_fees = request.POST.get('paid_fees')
        fees.save()

        return redirect('student_fees', id=fees.student.id)

    return render(request, 'fees/update_fees.html', {
        'fees': fees
    })


# -------------------------
# Delete Fees
# -------------------------
@login_required(login_url='/accounts/login/')
def delete_fees(request, id):
    fees = get_object_or_404(Fees, id=id)
    student_id = fees.student.id
    fees.delete()

    return redirect('student_fees', id=student_id)