from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),

    path('add/', views.add_student, name='add_student'),

    path('update/<int:id>/', views.update_student, name='update_student'),

    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    path('dashboard/', views.student_dashboard, name='student_dashboard'),

    # TEACHER CONTROL PANEL
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    path('manage/<int:id>/', views.manage_student, name='manage_student'),
    path('manage/<int:id>/add-attendance/', views.add_attendance),
path('manage/<int:student_id>/add-marks/', views.add_marks),
path('manage/<int:student_id>/add-fees/', views.add_fees),
]