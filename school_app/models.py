from django.db import models

class School(models.Model):
    name = models.CharField(max_length=20)
    head_of_school = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name