from django.db import models
from teacher.models import Teacher

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


class SchoolYear(models.Model):
    TERM_CHOICES = (
        ('I', 'Học kì I'),
        ('II', 'Học kì II'),
        ('III', 'Học kì III'),
        ('IV', 'Học kì IV'),
        ('KP', 'Học kì phụ'),
        ('CC', 'Chứng chỉ & Sát hạch'),
    )
    name = models.CharField(max_length=50, null=True, blank=True)
    term = models.CharField(max_length=10, choices=TERM_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.term}'


class Subjects(models.Model):
    studies = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=150)
    specialization = models.ManyToManyField(Specialization, null=True)
    credits = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name