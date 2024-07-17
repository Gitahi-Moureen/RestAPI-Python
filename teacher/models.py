from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=20)
    teacher_Id = models.PositiveSmallIntegerField()
    email = models.EmailField()
    nationality = models.CharField(max_length=20)
    specialization = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    years_of_experience = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

# Create your models here.
