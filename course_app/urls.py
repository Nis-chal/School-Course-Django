from django.urls import path
from .views import *


urlpatterns = [
    path("create", createCourse , name="course_create"),
    path("update/<int:courseId>", updateCourse ,name="course_update"),
    path("detail/<int:courseId>", getCourseDetail,name="course_detail"),
    path("list", getCourseList , name="course_list"),
    path('delete/<int:courseId>', courseDelete, name ='course_delete'),
]