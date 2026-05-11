from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Student

from .forms import StudentForm

from accounts.decorators import allowed_users


# =========================
# VIEW ALL STUDENTS
# =========================



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def student_list(request):

    query = request.GET.get('q')

    students = Student.objects.all()

    if query:

        students = Student.objects.filter(

            name__icontains=query

        ) | Student.objects.filter(

            rollno__icontains=query

        ) | Student.objects.filter(

            course__icontains=query
        )

    return render(request, 'student_list.html', {

        'students': students

    })

# =========================
# ADD STUDENT
# =========================

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
@allowed_users(allowed_roles=['teacher', 'admin'])
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('/students/')
# Create your views here.
