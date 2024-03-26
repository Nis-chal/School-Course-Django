from django.urls import path
from .views import *


urlpatterns = [
    path("list", getSchoolList ,name="school_list"),
    path("detail/<int:schoolId>", getSchoolDetail,name="school_detail"),
    path("create", addSchool ,name="school_create"),
    path("update/<int:schoolId>", updateSchool ,name="school_update"),
    path('delete/<int:schoolId>', schoolDelete, name ='school_delete'),
    
 
]
