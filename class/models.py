from django.db import models


class Class(models.Model):
    class_name = models.CharField(max_length=20)
    class_color = models.CharField(max_length=20)
    class_building = models.CharField()
    class_size = models.PositiveSmallIntegerField()
    class_capacity = models.PositiveSmallIntegerField()
    class_lighting = models.CharField()
    class_temperature = models.CharField()
    class_odor = models.CharField()
    class_comfort = models.CharField()
    class_state = models.CharField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
# Create your models here.
