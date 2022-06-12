from re import template
from django.shortcuts import render
from .forms import StudentForm
from .models import *
# Create your views here.

def AddStudentView(request):
    template_name='app1/addstudent.html'
    form = StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST, request.FILES) #Added request.FILES
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,template_name,context)

def ShowStudent(request):
    data=Student.objects.all()
    template_name='app1/showstudent.html'
    context={'obj':data}
    return render(request,template_name,context)
