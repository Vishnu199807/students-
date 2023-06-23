from django.contrib import admin
from students.models import Student


# Register your models here.

class studententery(admin.ModelAdmin):
    student_details = ['admission_no ','full_name,email','age,student_class' ,'description','image,marklist']


admin.site.register(Student,studententery)