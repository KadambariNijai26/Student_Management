from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from students.models import Student
from .models import Attendance


@login_required(login_url='/accounts/login/')
def attendance_view(request, id):
    student = get_object_or_404(Student, id=id)

    records = Attendance.objects.filter(student=student)

    total = records.count()
    present = records.filter(status='Present').count()

    percentage = (present / total) * 100 if total > 0 else 0

    return render(request, 'attendance.html', {
        'student': student,
        'records': records,
        'percentage': percentage
    })
@login_required(login_url='/accounts/login/')
def update_attendance(request, id):

    attendance = get_object_or_404(Attendance, id=id)

    if request.method == "POST":
        attendance.status = request.POST['status']
        attendance.save()
        return redirect('/students/manage/' + str(attendance.student.id))

    return render(request, 'update_attendance.html', {
        'attendance': attendance
    })

@login_required(login_url='/accounts/login/')

def delete_attendance(request, id):
    _ = request
    attendance = get_object_or_404(Attendance, id=id)
    student_id = attendance.student.id
    attendance.delete()
    return redirect('/students/manage/' + str(student_id))

def add_attendance(request, id):
    student = get_object_or_404(Student, id=id)
    # your logic here
    return render(request, 'add_attendance.html', {'student': student})
# Create your views here.
