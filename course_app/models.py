from django.db import models
from school_app.models import School
from django.core.validators import MinValueValidator, MaxValueValidator

class Course(models.Model):
    name = models.CharField(max_length=20)
    coordinator = models.CharField(max_length=20)
    credits = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(360)]) 
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name
