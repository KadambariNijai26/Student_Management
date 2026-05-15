from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
]