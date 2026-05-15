from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from .models import Fees

@login_required(login_url='/accounts/login/')

def fees_view(request):

    data = Fees.objects.all()
    print(data)

    return render(request, 'fees.html', {
        'data': data
    })



def update_fees(request, id):

    fees = get_object_or_404(Fees, id=id)

    if request.method == "POST":
        fees.total_fees = request.POST['total_fees']
        fees.paid_fees = request.POST['paid_fees']
        fees.save()

        return redirect('/students/manage/' + str(fees.student.id))

    return render(request, 'update_fees.html', {
        'fees': fees
    })

def delete_fees(request, id):
    fees = get_object_or_404(Fees, id=id)
    student_id = fees.student.id
    fees.delete()
    return redirect('/students/manage/' + str(student_id))
# Create your views here.
