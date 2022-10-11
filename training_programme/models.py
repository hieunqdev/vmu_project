from operator import mod
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50, null=True, blank=True)
    head_of_department = models.CharField(max_length=150, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    studies = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.department} - {self.name}'

class SpecializationClass(models.Model):
    TYPE_OF_TRAINING_CHOICES = (
        ('ThS', 'Thạc sĩ'),
        ('TS', 'Tiến sĩ'),
    )
    specialization = models.ManyToManyField(Specialization, null=True)
    name = models.CharField(max_length=10, choices=TYPE_OF_TRAINING_CHOICES)

    def __str__(self):
        return self.name