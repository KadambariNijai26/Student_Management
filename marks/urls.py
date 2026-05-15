from django.urls import path
from . import views

urlpatterns = [
    path('', views.marks_view, name='marks'),
    path('update/<int:id>/', views.update_marks, name='update_marks'),
    path('delete/<int:id>/', views.delete_marks),
]