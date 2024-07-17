from django.urls import path
from api.views import StudentListView
from api.views import ClassPeriodListView
from api.views import  TeacherListView

urlpatterns = [
    path("student/", StudentListView.as_view(), name = "student_list_view"),
    path('classperiod/', ClassPeriodListView.as_view(), name='classperiod_list_view'),
    path("teacher/", TeacherListView.as_view(), name="teacher_list_view"),
   
]
