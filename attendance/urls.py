from django.urls import path
from . import views

urlpatterns = [

    # 📌 Teacher sees list of students
    path('', views.attendance_students, name='attendance_students'),

    # 📌 Single student attendance
    path('student/<int:id>/', views.student_attendance, name='student_attendance'),

    # 📌 Add attendance for student
    path('add/<int:id>/', views.add_attendance, name='add_attendance'),

    # 📌 Update attendance
    path('update/<int:id>/', views.update_attendance, name='update_attendance'),

    # 📌 Delete attendance
    path('delete/<int:id>/', views.delete_attendance, name='delete_attendance'),
]