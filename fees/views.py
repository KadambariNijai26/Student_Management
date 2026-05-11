from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Fees


@login_required(login_url='/login/')
def fees_view(request):

    data = Fees.objects.all()

    return render(request, 'fees.html', {
        'data': data
    })
# Create your views here.
