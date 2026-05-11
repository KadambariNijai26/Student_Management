"""
URL configuration for sms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

 
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from core import views as core

from attendance.views import attendance_view
from marks.views import marks_view
from fees.views import fees_view

from accounts.views import (
    login_view,
    register,
    logout_view,
    student_dashboard,
    teacher_dashboard,
    admin_dashboard,
    profile
)
from students.views import (

    student_list,

    add_student,

    update_student,

    delete_student

)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', core.home, name='home'),

    path('about/', core.about, name='about'),

    path('contact/', core.contact, name='contact'),

    path('attendance/', attendance_view, name='attendance'),

    path('marks/', marks_view, name='marks'),

    path('fees/', fees_view, name='fees'),

    path('login/', login_view, name='login'),

    path('register/', register, name='register'),

    path('logout/', logout_view, name='logout'),

    path('student-dashboard/', student_dashboard),

    path('teacher-dashboard/', teacher_dashboard),

    path('admin-dashboard/', admin_dashboard),

    path('profile/', profile),


    path('students/', student_list),

    path('add-student/', add_student),

    path('update-student/<int:id>/', update_student),

    path('delete-student/<int:id>/', delete_student),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)