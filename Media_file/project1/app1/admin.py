from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['sid','name','branch','photo','dmc']

admin.site.register(Student,StudentAdmin)