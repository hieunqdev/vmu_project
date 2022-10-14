from django.shortcuts import render
from django.views import View
from .models import Specialization

# Create your views here.
class View_training_programme(View):
    def get(self, request):
        specializations = Specialization.objects.raw("SELECT training_programme_specialization.id, training_programme_specialization.name AS ten_nganh, training_programme_specialization.studies AS ma_nganh, CASE WHEN (training_programme_specializationclass.name LIKE ('ThS')) THEN 'Thạc sĩ' ELSE 'Tiến sĩ' END AS trinh_do FROM training_programme_specialization INNER JOIN training_programme_specializationclass_specialization ON training_programme_specialization.id = training_programme_specializationclass_specialization.specialization_id INNER JOIN training_programme_specializationclass ON training_programme_specializationclass_specialization.specializationclass_id = training_programme_specializationclass.id;")
        context = {
            'specializations': specializations
        }
        return render(request, 'training_programme.html', context)
