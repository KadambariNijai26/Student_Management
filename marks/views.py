from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Marks


@login_required(login_url='/accounts/login/')
def marks_view(request):

    data = Marks.objects.all()


    return render(request, 'marks.html', {
        'data': data
    })



def add_marks(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        Marks.objects.create(
            student=student,
            subject=request.POST['subject'],
            marks=request.POST['marks']
        )
        return redirect('/students/manage/' + str(id))

    return render(request, 'accounts/form.html', {
        'student': student
    })

def update_marks(request, id):

    marks = get_object_or_404(Marks, id=id)

    if request.method == "POST":
        marks.subject = request.POST['subject']
        marks.marks = request.POST['marks']
        marks.save()

        return redirect('/students/manage/' + str(marks.student.id))

    return render(request, 'update_marks.html', {
        'marks': marks
    })


def delete_marks(request, id):
    marks = get_object_or_404(Marks, id=id)
    student_id = marks.student.id
    marks.delete()
    return redirect('/students/manage/' + str(student_id))

# Create your views here.
