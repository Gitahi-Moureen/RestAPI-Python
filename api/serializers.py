from rest_framework import serializers
from student.models import Student
from classperiod.models import ClassPeriod
from teacher.models import Teacher
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        field = "__all__"

