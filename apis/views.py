from django.shortcuts import render
from training_programme.models import Department, Specialization, Subjects
from news.models import Notification
from .serializers import DepartmentSerializer, SpecializationSerializer, SubjectsSerializer, NotificationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def department_list(request):

    if request.method == 'GET':
        department = Department.objects.all().values('name', 'head_of_department')
        specialization = Specialization.objects.all()

        serializer_d = DepartmentSerializer(department, many=True)
        serializer_s = SpecializationSerializer(specialization, many=True)
        return Response({
            'department': serializer_d.data,
            'specialization': serializer_s.data,
        })
    

@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail(request, id):

    try:
        subject = Subjects.objects.get(pk=id)
    except Subjects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectsSerializer(subject)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SubjectsSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def notification_list(request):

    if request.method == 'GET':
        notification = Notification.objects.all()
        serializer = NotificationSerializer(notification, many=True)
        return Response({
            'department': serializer.data,
        })
