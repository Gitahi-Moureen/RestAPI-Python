from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.modelSerializer):
    class Meta:
        model = Student
        field = "__all__"