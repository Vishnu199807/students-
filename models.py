from django.db import models


class Student(models.Model):
    ADMISSION_CHOICES = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
        ('9', '9th'),
        ('10', '10th'),
        ('11', '11th'),
        ('12', '12th'),

    )
    admission_no = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    student_class = models.CharField(max_length=2, choices=ADMISSION_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    marklist = models.FileField(upload_to='documents/')



