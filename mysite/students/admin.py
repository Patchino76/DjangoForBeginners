from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['department_name']