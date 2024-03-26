from django.db import models
from school_app.models import School

class Course(models.Model):
    name = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    credits = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name