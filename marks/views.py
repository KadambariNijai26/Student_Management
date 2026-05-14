from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Marks


@login_required(login_url='/accounts/login/')
def marks_view(request):

    data = Marks.objects.all()

    return render(request, 'marks.html', {
        'data': data
    })
# Create your views here.
