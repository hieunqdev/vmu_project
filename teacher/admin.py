from django.contrib import admin
from .models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'gender', 'phone', 'email', 'address']
    list_filter = ['name', 'date_of_birth', 'gender', 'phone', 'email', 'address']

admin.site.register(Teacher, TeacherAdmin)