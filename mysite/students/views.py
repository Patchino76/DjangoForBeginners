from django.shortcuts import render
from django.http import HttpResponse
# from types import NoneType
from .models import *
# Create your views here.

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def student(request, id = 0): 
    try:
        student = Student.objects.get(id = id)
    except Student.DoesNotExist: 		# if it doesn't find a matching object, return a 404 error.
        student = None
    return render(request, 'student.html', {'student': student})