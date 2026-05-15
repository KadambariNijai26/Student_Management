from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_view, name='attendance'),
    path('attendance/<int:id>/', views.attendance_view, name='attendance_view'),
    path('update/<int:id>/', views.update_attendance, name='update_attendance'),
    path('delete/<int:id>/', views.delete_attendance, name='delete_attendance'),
    path('add-attendance/<int:id>/', views.add_attendance, name='add_attendance'),
    
]