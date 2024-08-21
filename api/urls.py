from django.urls import path,include
from api.views import StudentListView
from api.views import ClassPeriodListView
from api.views import  TeacherListView
from .views import StudentDetailView

urlpatterns = [
    path("student/", StudentListView.as_view(), name = "student_list_view"),
    path("teacher/", TeacherListView.as_view(), name="teacher_list_view"),
    path("student/<int:id>/" , StudentDetailView.as_view(), name = "student_detail_view"),


   
]
