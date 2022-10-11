from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.forms import ChoiceField, DateField
from training_programme.models import Department, Specialization, SpecializationClass

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Nam'),
        ('F', 'Nữ'),
    )
    FOREIGN_LANGUAGE_CHOICES = (
        ('PASS', 'Đạt'),
        ('NOT PASS', 'Chưa đạt'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    studis = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    specializationClass = models.ForeignKey(SpecializationClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    date_of_birth = DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    base_point = models.FloatField(null=True, blank=True)
    foreign_language = models.CharField(max_length=10, choices=FOREIGN_LANGUAGE_CHOICES)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.studis} - {self.name}'


