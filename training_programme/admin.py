from django.contrib import admin
from .models import Department, Specialization, SpecializationClass, Subjects, SchoolYear

# Register your models here.
admin.site.register(Department)
admin.site.register(Specialization)
admin.site.register(SpecializationClass)
admin.site.register(Subjects)
admin.site.register(SchoolYear)