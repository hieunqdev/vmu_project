from django.contrib import admin
from .models import Department, Specialization, SpecializationClass

# Register your models here.
admin.site.register(Department)
admin.site.register(Specialization)
admin.site.register(SpecializationClass)