from django.urls import path
from .views import *

urlpatterns=[
    path('as/', AddStudentView, name='addstudent_url'),
    path('ss/',ShowStudent,name='showstudent_url'),
]