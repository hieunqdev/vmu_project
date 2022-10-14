from django.contrib import admin
from .models import Student, Scores

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['studis', 'name', 'date_of_birth', 'gender', 'department', 'specialization', 'specializationClass']
    list_filter = ['studis', 'name', 'date_of_birth', 'gender', 'department', 'specialization', 'specializationClass']

class ScoresAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'scores_x', 'scores_y', 'scores_z', 'grade', 'studies_again', 'exam_again']
    list_filter = ['student', 'subject', 'scores_x', 'scores_y', 'scores_z', 'grade', 'studies_again', 'exam_again']

admin.site.register(Student, StudentAdmin)
admin.site.register(Scores, ScoresAdmin)