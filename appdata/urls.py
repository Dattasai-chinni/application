from django.urls import path
from .views import create_employee

urlpatterns = [
    path('employees/', create_employee, name='create-employee'),
]
