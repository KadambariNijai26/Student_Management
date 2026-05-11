from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .decorators import allowed_users
from .models import UserProfile
from .forms import ProfileForm


# =========================
# REGISTER VIEW
# =========================

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        # Check username
        if User.objects.filter(username=username).exists():

            messages.error(request, 'Username already exists')

            return redirect('/register/')

        # Create User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create Profile
        UserProfile.objects.create(
            user=user,
            role=role
        )

        messages.success(request, 'Registration Successful')

        return redirect('/login/')

    return render(request, 'register.html')


# =========================
# LOGIN VIEW
# =========================

def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # SAFE PROFILE CREATION
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    'role': 'student',
                    'phone': '',
                    'address': ''
                }
            )

            # ROLE REDIRECT
            if profile.role == 'student':

                return redirect('/student-dashboard/')

            elif profile.role == 'teacher':

                return redirect('/teacher-dashboard/')

            elif profile.role == 'admin':

                return redirect('/admin-dashboard/')

            return redirect('/')

        else:

            messages.error(request, 'Invalid Username or Password')

            return redirect('/login/')

    return render(request, 'login.html')


# =========================
# LOGOUT VIEW
# =========================

def logout_view(request):

    logout(request)

    messages.success(request, 'Logged Out Successfully')

    return redirect('/login/')


# =========================
# STUDENT DASHBOARD
# =========================

@login_required(login_url='/login/')
def student_dashboard(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'role': 'student'
        }
    )

    if profile.role != 'student':

        return HttpResponse("Unauthorized Access")

    return render(request, 'student_dashboard.html')


# =========================
# TEACHER DASHBOARD
# =========================

@login_required(login_url='/login/')
def teacher_dashboard(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'role': 'teacher'
        }
    )

    if profile.role != 'teacher':

        return HttpResponse("Unauthorized Access")

    return render(request, 'teacher_dashboard.html')


# =========================
# ADMIN DASHBOARD
# =========================

@login_required(login_url='/login/')
def admin_dashboard(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'role': 'admin'
        }
    )

    if profile.role != 'admin':

        return HttpResponse("Unauthorized Access")

    return render(request, 'admin_dashboard.html')


# =========================
# PROFILE VIEW
# =========================

@login_required(login_url='/login/')
def profile(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'role': 'student',
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

        return redirect('/profile/')

    return render(request, 'profile.html', {
        'form': form,
        'profile': profile
    })
    
