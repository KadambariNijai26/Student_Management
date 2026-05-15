from django.urls import path
from . import views

urlpatterns = [
    path('', views.fees_view, name='fees'),
    path('update/<int:id>/', views.update_fees, name='update_fees'),
    path('delete/<int:id>/', views.delete_fees),
]