from django.urls import path

from .views import Employees

app_name = 'employees'

urlpatterns = [
    path('', Employees.as_view(), name='employees')
]
