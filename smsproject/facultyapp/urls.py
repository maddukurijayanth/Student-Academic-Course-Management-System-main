from django.urls import path
from . import views
urlpatterns = [
    path("checkfacultylogin", views.checkfacultylogin, name="checkfacultylogin"),
    path("facultyhome",views.facultyhome,name="facultyhome"),
    path("facultycourses",views.facultycourses,name="facultycourses"),
    path("facultychangepwd", views.facultychangepwd, name="facultychangepwd"),
    path("facultyupdatepwd", views.facultyupdatepwd, name="facultyupdatepwd"),
]