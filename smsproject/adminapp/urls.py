
from django.urls import path
from . import views

urlpatterns = [
    path("adminhome", views.adminhome, name= "adminhome"),
    path("adminlogout", views.logout, name= "adminlogout"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("adminchangepwd",views.adminchangepwd,name="adminchangepwd"),
    path("adminupdatepwd", views.adminupdatepwd, name="adminupdatepwd"),
    path("admincourse",views.admincourse,name="admincourse"),
    path("viewcourses",views.viewcourses,name="viewcourses"),
    path("addcourse",views.addcourse,name="addcourse"),
    path("insertcourse",views.insertcourse,name="insertcourse"),
    path("deletecourse",views.deletecourse,name="deletecourse"),
    path("coursedeletion/<int:cid>",views.coursedeletion,name="coursedeletion"),
    path("updatecourse",views.updatecourse,name="updatecourse"),
    path("courseupdation/<int:cid>",views.courseupdation,name="courseupdation"),
    path("courseupdated",views.courseupdated,name="courseupdated"),
    path("adminstudent",views.adminstudent,name="adminstudent"),
    path("viewstudents",views.viewstudents,name="viewstudents"),
    path("addstudent",views.addstudent,name="addstudent"),
    path("deletestudent", views.deletestudent, name="deletestudent"),
    path("studentdeletion/<int:sid>", views.studentdeletion, name="studentdeletion"),
    path("updatestudent",views.updatestudent,name="updatestudent"),
    path("studentupdation/<int:sid>",views.studentupdation,name="studentupdation"),

    path("adminfaculty",views.adminfaculty,name="adminfaculty"),
    path("viewfaculty",views.viewfaculty,name="viewfaculty"),
    path("addfaculty",views.addfaculty,name="addfaculty"),
    path("deletefaculty", views.deletefaculty, name="deletefaculty"),
    path("facultydeletion/<int:fid>", views.facultydeletion, name="facultydeletion"),
    path("updatefaculty", views.updatefaculty, name="updatefaculty"),
    path("facultyupdation/<int:fid>", views.facultyupdation, name="facultyupdation"),
    path("facultycoursemapping",views.facultycoursemapping,name="facultycoursemapping"),
]
