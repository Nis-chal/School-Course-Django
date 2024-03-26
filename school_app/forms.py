from django import forms

from .models import School

class SchoolForm(forms.ModelForm):
       class Meta:
        model = School
        fields = ['name','head_of_school','location']