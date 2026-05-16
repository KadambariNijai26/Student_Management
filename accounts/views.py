from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserProfile
from .forms import ProfileForm
from students.models import Course


# =========================
# REGISTER VIEW (UPDATED WITH COURSE SUPPORT)
# =========================



def register_view(request):

    if request.method == 'POST':

        try:

            username = request.POST.get('username').strip()
            email = request.POST.get('email').strip()
            password = request.POST.get('password')
            role = request.POST.get('role')
            
            course_id = request.POST.get('course')

            course = Course.objects.get(id=course_id) # ✅ ADDED COURSE

            if User.objects.filter(username=username).exists():

                messages.error(request, 'Username already exists')
                return redirect('/accounts/register/')

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # ✅ SAVE PROFILE WITH COURSE
            UserProfile.objects.create(
                user=user,
                role=role,
                course=course,   # IMPORTANT
                phone='',
                address=''
            )

            messages.success(request, 'Registration successful')

            return redirect('/accounts/login/')

        except Exception as e:
            return HttpResponse(str(e))

    return render(request, 'accounts/register.html', {
    'courses': Course.objects.all()
})


# =========================
# LOGIN VIEW
# =========================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    'role': 'student',
                    'course': '',   # ✅ ADDED COURSE DEFAULT
                    'phone': '',
                    'address': '',
                }
            )

            if profile.role == 'teacher':
                return redirect('/accounts/teacher-dashboard/')

            elif profile.role == 'admin':
                return redirect('/accounts/admin-dashboard/')

            else:
                return redirect('/accounts/student-dashboard/')

        else:
            messages.error(request, 'Invalid Username or Password')

    return render(request, 'accounts/login.html')


# =========================
# LOGOUT VIEW
# =========================

def logout_view(request):

    logout(request)

    messages.success(request, 'Logged Out Successfully')

    return redirect('/accounts/login/')


# =========================
# STUDENT DASHBOARD
# =========================

@login_required(login_url='/accounts/login/')
def student_dashboard(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'role': 'student',
            'course': '',
            'phone': '',
            'address': ''
        }
    )

    if profile.role != 'student':
        return HttpResponse("Unauthorized Access")

    return render(request, 'accounts/student_dashboard.html')


# =========================
# TEACHER DASHBOARD
# =========================

@login_required(login_url='/accounts/login/')
def teacher_dashboard(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'role': 'teacher',
            'course': '',   # IMPORTANT
            'phone': '',
            'address': ''
        }
    )

    if profile.role != 'teacher':
        return HttpResponse("Unauthorized Access")

    return render(request, 'accounts/teacher_dashboard.html')


# =========================
# ADMIN DASHBOARD
# =========================

@login_required(login_url='/accounts/login/')
def admin_dashboard(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'role': 'admin',
            'course': '',
            'phone': '',
            'address': ''
        }
    )

    if profile.role != 'admin':
        return HttpResponse("Unauthorized Access")

    return render(request, 'accounts/admin_dashboard.html')


# =========================
# PROFILE VIEW
# =========================

@login_required(login_url='/accounts/login/')
def profile(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'role': 'student',
            'course': '',
            'phone': '',
            'address': ''
        }
    )

    form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=profile
    )

    if form.is_valid():
        form.save()
        messages.success(request, 'Profile Updated Successfully')
        return redirect('/accounts/profile/')

    return render(request, 'profile.html', {
        'form': form,
        'profile': profile
    })