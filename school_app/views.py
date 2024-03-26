from django.shortcuts import render,redirect,get_object_or_404
from .models import School
from course_app.models import Course
from .forms import SchoolForm 
from django.db.models import Prefetch

# Create your views here.

app_name = 'school_app'

def addSchool (request):
    if request.method == 'POST':
        school_form = SchoolForm(request.POST)
        if school_form.is_valid():
            school = school_form.save(commit= False)
    
      
        return redirect('/school/detail/{}'.format(school.id))
    else:
        form = SchoolForm()
        return render(request, 'school_add.html',{'school_form': form})
    
def getSchoolList (request):
    schools = School.objects.all().prefetch_related(
        Prefetch('courses', queryset=Course.objects.all())
    )
    
    context ={
        'schools':schools
    }
    return render(request, 'school_list.html',context)

def getSchoolDetail(request, schoolId):
    school = get_object_or_404(School, pk=schoolId)

    courses = Course.objects.filter(school=schoolId)

    return render(request, 'school_detail.html', {"schoolDetails": school, "courses": courses})
    

def updateSchool (request,schoolId):
    school_instance = get_object_or_404(School, pk=schoolId)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school_instance)
        if form.is_valid():
            form.save()
            return redirect('/school/detail/{}'.format(school_instance.id))  # Redirect to a success URL
    else:
        form = SchoolForm(instance=school_instance)  # Populate the form with the instance data
    return render(request, 'school_edit.html', {'school_form': form})
    


def schoolDelete(request,schoolId):
    if request.method == 'POST':
      school = get_object_or_404(School, pk=schoolId)
      school.delete()
      return redirect('/school/list')
    else:
        return redirect('/school/list')
    

