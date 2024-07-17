from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer,TeacherSerializer ,StudentSerializer
from rest_framework.response import Response 

class ClassPeriodListView(APIView):
    def get(self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many = True)
        return Response(serializer.data)

class StudentListView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students , many= True)
        return Response(serializer.data)

class TeacherListView(APIView):
    def get(self,request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(students , many= True)
        return Response(serializer.data)

