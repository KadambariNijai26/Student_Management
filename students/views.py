from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Student

from .forms import StudentForm

from accounts.decorators import allowed_users
from attendance.models import Attendance
from marks.models import Marks
from fees.models import Fees
from attendance.forms import AttendanceForm
from marks.forms import MarksForm
from fees.forms import FeesForm


# =========================
# VIEW ALL STUDENTS
# =========================



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def student_list(request):

    query = request.GET.get('q')

    students = Student.objects.all()

    if query:

        students = Student.objects.filter(

            name__icontains=query

        ) | Student.objects.filter(

            roll_no__icontains=query

        ) | Student.objects.filter(

            course__icontains=query
        )

    return render(request, 'student_list.html', {

        'students': students

    })

# =========================
# ADD STUDENT
# =========================

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def add_student(request):

    form = StudentForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('/students/')

    return render(request, 'add_student.html', {

        'form': form

    })


# =========================
# UPDATE STUDENT
# =========================

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    form = StudentForm(

        request.POST or None,

        instance=student
    )

    if form.is_valid():

        form.save()

        return redirect('/students/')

    return render(request, 'update_student.html', {

        'form': form

    })


# =========================
# DELETE STUDENT
# =========================

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('/students/')


# =========================
# STUDENT DASHBOARD
# =========================

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['student'])
def student_dashboard(request):

    try:
        student = Student.objects.get(user=request.user)

        attendance = Attendance.objects.filter(student=student)

        marks = Marks.objects.filter(student=student)

        fees = Fees.objects.filter(student=student)
        print(fees)

        context = {
            'student': student,
            'attendance': attendance,
            'marks': marks,
            'fees': fees,
        }

        return render(request, 'student_dashboard.html', context)

    except Student.DoesNotExist:

        return render(request, 'error.html', {
            'message': 'Student profile not found'
        })
    

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def teacher_dashboard(request):
    students = Student.objects.all()

    return render(request, 'teacher_dashboard.html', {
        'students': students
    })   

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def manage_student(request, id):

    student = get_object_or_404(Student, id=id)

    attendance = Attendance.objects.filter(student=student)
    marks = Marks.objects.filter(student=student)
    fees = Fees.objects.filter(student=student)

    return render(request, 'manage_student.html', {
        'student': student,
        'attendance': attendance,
        'marks': marks,
        'fees': fees,
    }) 


@login_required
@allowed_users(allowed_roles=['teacher', 'admin'])
def add_attendance(request, student_id):

    student = Student.objects.get(id=student_id)

    form = AttendanceForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.student = student
        obj.save()
        return redirect('/students/manage/' + str(student.id))

    return render(request, 'form.html', {'form': form})


@login_required
@allowed_users(allowed_roles=['teacher', 'admin'])
def add_marks(request, student_id):

    student = Student.objects.get(id=student_id)

    form = MarksForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.student = student
        obj.save()
        return redirect('/students/manage/' + str(student.id))

    return render(request, 'form.html', {'form': form})



@login_required
@allowed_users(allowed_roles=['teacher', 'admin'])
def add_fees(request, student_id):

    student = Student.objects.get(id=student_id)

    form = FeesForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.student = student
        obj.save()
        return redirect('/students/manage/' + str(student.id))

    return render(request, 'form.html', {'form': form})
# Create your views here.
