from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_view, name='attendance'),
    path('add-attendance/', views.add_attendance),
    path('update/<int:id>/', views.update_attendance, name='update_attendance'),
    path('delete/<int:id>/', views.delete_attendance, name='delete_attendance'),
    
    
]