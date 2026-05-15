from django.urls import path
from . import views

urlpatterns = [

    # 📌 Student list for marks
    path('', views.marks_students, name='marks_students'),

    # 📌 Student-wise marks view
    path('student/<int:id>/', views.student_marks, name='student_marks'),

    # 📌 Add marks for student
    path('add/<int:id>/', views.add_marks, name='add_marks'),

    # 📌 Update marks
    path('update/<int:id>/', views.update_marks, name='update_marks'),

    # 📌 Delete marks
    path('delete/<int:id>/', views.delete_marks, name='delete_marks'),
]