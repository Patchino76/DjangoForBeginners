from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'), ('F', 'Female'), ('O', 'Other')  # 	Mērējais/Frau
    ]
    first_name = models.CharField(max_length=30) # name of the person 
    last_name = models.CharField(max_length=30)
    email_id= models.EmailField() # this is the email field for the user to input their email address to sign in with.
    phone_number = models.CharField(max_length=15) # this is the field for the user to input their contact number.
    gender = models.CharField(choices = GENDER_CHOICES, max_length=1) # this is the field for the user to input their gender.
    address = models.TextField() # this is the field for the user to input their address. 	It is a long text field. 	It can
    department = models.ManyToManyField('Departments')
    date_of_birth = models.DateField() # this is the field for the user to input their date of birth. 	It can be parsed into
    
class Departments(models.Model):
    department_name = 	 models.CharField(max_length=30) # this is the field for the user to input their department. 	It can be parsed into