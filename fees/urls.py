from django.urls import path
from . import views

urlpatterns = [

    # 📌 Student list (Fees module)
    path('', views.fees_students, name='fees_students'),

    # 📌 Student-wise fees view
    path('student/<int:id>/', views.student_fees, name='student_fees'),

    # 📌 Add fees for student
    path('add/<int:id>/', views.add_fees, name='add_fees'),

    # 📌 Update fees
    path('update/<int:id>/', views.update_fees, name='update_fees'),

    # 📌 Delete fees
    path('delete/<int:id>/', views.delete_fees, name='delete_fees'),
]