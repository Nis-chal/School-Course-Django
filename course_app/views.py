from django.shortcuts import render, redirect, get_object_or_404

from .models import Course
from .forms import CourseForm

# Create your views here.

app_name = 'course_app'
def createCourse(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course = course_form.save(commit= False)
            course.save()
            return redirect('/course/detail/{}'.format(course.id))  # Redirect to a success page or another view
    else:
        school_form = CourseForm()
    return render(request, 'course_add.html', {'course_form': school_form})


def getCourseDetail(request,courseId):
    courseDetail = get_object_or_404(Course, pk=courseId)
    
    return render(request, 'course_detail.html',{"courseDetails":courseDetail})


def getCourseList(request):
    courseList = Course.objects.all()
    context ={
        'courseList':courseList
    }
    return render(request, 'course_list.html',context)


def updateCourse (request,courseId):
    course_instance = get_object_or_404(Course, pk=courseId)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course_instance)
        if form.is_valid():
            form.save()
            return redirect('/course/detail/{}'.format(course_instance.id))  # Redirect to a success URL
    else:
        form = CourseForm(instance=course_instance)  # Populate the form with the instance data
    return render(request, 'course_edit.html', {'course_form': form})


def courseDelete(request,courseId):
    if request.method == 'POST':
      course = get_object_or_404(Course, pk=courseId)
      course.delete()
      return redirect('/course/list')
    else:
        return redirect('/course/list')
