from django.urls import path
from . import views

urlpatterns = [
    path('', views.marks_view, name='marks'),
]