from django.shortcuts import render
from django.views import View
from .models import Student
from training_programme.models import SchoolYear

# Create your views here.
class Scores(View):
    def get(self, request):
        # id user login
        user = request.user
        # infomation of student with student_id = id login
        information_student = Student.objects.filter(user_id=user.id).values()
        # specialization of student login
        specializations = Student.objects.raw('SELECT student_student.user_id, training_programme_specialization.name FROM training_programme_specialization INNER JOIN student_student ON student_student.specialization_id = training_programme_specialization.id WHERE student_student.user_id=%s;', [user.id])

        # get scores of a student
        scores_1styear_term1 = SchoolYear.objects.raw("SELECT training_programme_schoolyear.id, student_scores.student_id, training_programme_schoolyear.name AS name_year, training_programme_schoolyear.term, training_programme_subjects.studies, training_programme_subjects.name AS name_subject, training_programme_subjects.credits, student_scores.scores_x, student_scores.scores_y, student_scores.scores_z, student_scores.grade FROM training_programme_schoolyear INNER JOIN training_programme_subjects ON training_programme_schoolyear.id = training_programme_subjects.school_year_id INNER JOIN student_scores ON training_programme_subjects.id = student_scores.subject_id WHERE student_scores.student_id = %s AND training_programme_schoolyear.term LIKE ('I');", [user.id])
        scores_1styear_term2 = SchoolYear.objects.raw("SELECT training_programme_schoolyear.id, student_scores.student_id, training_programme_schoolyear.name AS name_year, training_programme_schoolyear.term, training_programme_subjects.studies, training_programme_subjects.name AS name_subject, training_programme_subjects.credits, student_scores.scores_x, student_scores.scores_y, student_scores.scores_z, student_scores.grade FROM training_programme_schoolyear INNER JOIN training_programme_subjects ON training_programme_schoolyear.id = training_programme_subjects.school_year_id INNER JOIN student_scores ON training_programme_subjects.id = student_scores.subject_id WHERE student_scores.student_id = %s AND training_programme_schoolyear.term LIKE ('II');", [user.id])
        scores_2ndyear_term3 = SchoolYear.objects.raw("SELECT training_programme_schoolyear.id, student_scores.student_id, training_programme_schoolyear.name AS name_year, training_programme_schoolyear.term, training_programme_subjects.studies, training_programme_subjects.name AS name_subject, training_programme_subjects.credits, student_scores.scores_x, student_scores.scores_y, student_scores.scores_z, student_scores.grade FROM training_programme_schoolyear INNER JOIN training_programme_subjects ON training_programme_schoolyear.id = training_programme_subjects.school_year_id INNER JOIN student_scores ON training_programme_subjects.id = student_scores.subject_id WHERE student_scores.student_id = %s AND training_programme_schoolyear.term LIKE ('III');", [user.id])
        scores_2ndyear_term4 = SchoolYear.objects.raw("SELECT training_programme_schoolyear.id, student_scores.student_id, training_programme_schoolyear.name AS name_year, training_programme_schoolyear.term, training_programme_subjects.studies, training_programme_subjects.name AS name_subject, training_programme_subjects.credits, student_scores.scores_x, student_scores.scores_y, student_scores.scores_z, student_scores.grade FROM training_programme_schoolyear INNER JOIN training_programme_subjects ON training_programme_schoolyear.id = training_programme_subjects.school_year_id INNER JOIN student_scores ON training_programme_subjects.id = student_scores.subject_id WHERE student_scores.student_id = %s AND training_programme_schoolyear.term LIKE ('IV');", [user.id])
        check_language = Student.objects.raw("SELECT student_student.user_id, CASE WHEN (student_student.foreign_language LIKE ('PASS')) THEN 'Đạt' ELSE 'Chưa đạt' END AS check_language FROM student_student WHERE user_id=%s;", [user.id])

        context = {
            'information_student': information_student,
            'specializations': specializations,
            'scores_1styear_term1': scores_1styear_term1,
            'scores_1styear_term2': scores_1styear_term2,
            'scores_2ndyear_term3': scores_2ndyear_term3,
            'scores_2ndyear_term4': scores_2ndyear_term4,
            'check_language': check_language
        }
        return render(request, 'scores.html', context)
