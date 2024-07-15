from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_description = models.CharField(max_length=20)
    course_level = models.CharField()
    course_duration = models.PositiveSmallIntegerField()
    course_objectives = models.CharField()
    course_module = models.CharField()
    course_prior_Skills = models.CharField()
    course_learning_materials = models.CharField()
    course_trainer = models.CharField()
    course_attendance = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

# Create your models here.
