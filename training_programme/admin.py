from django.contrib import admin
from .models import Department, Specialization, SpecializationClass, Subjects, SchoolYear

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields if field.name != "id"]
    list_filter = [field.name for field in Department._meta.fields if field.name != "id"]

class SpecializationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Specialization._meta.fields if field.name != "id"]
    list_filter = [field.name for field in Specialization._meta.fields if field.name != "id"]

class SpecializationClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SpecializationClass._meta.fields if field.name != "id"]
    list_filter = [field.name for field in SpecializationClass._meta.fields if field.name != "id"]

class SubjectsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subjects._meta.fields if field.name != "id"]
    list_filter = [field.name for field in Subjects._meta.fields if field.name != "id"]

class SchoolYearAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SchoolYear._meta.fields if field.name != "id"]
    list_filter = [field.name for field in SchoolYear._meta.fields if field.name != "id"]

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(SpecializationClass, SpecializationClassAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)