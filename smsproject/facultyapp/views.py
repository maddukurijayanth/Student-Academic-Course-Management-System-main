from django.shortcuts import render
from django.db.models import Q
from adminapp.models import Faculty,FacultyCourseMapping,Course


def checkfacultylogin(request):
    if request.method == "POST":
        fid = request.POST.get('fid')
        pwd = request.POST.get('pwd')

        flag = Faculty.objects.filter(Q(facultyid=fid) & Q(password=pwd)) # max 1 object
        print(flag)

        if flag:
            print("login success")
            request.session["fid"] = fid #creating session variable (auname)
            return render(request, "facultyhome.html",{"fid":fid})
        else:
                msg = "Login Failed"
                return render(request,"facultylogin.html",{"message":msg})

def facultyhome(request) :
    fid = request.session["fid"]
    return render(request,"facultyhome.html",{"fid":fid})
def facultycourses(request):
    fid = request.session["fid"]
    print(fid)
    courses = Course.objects.all()
    count = Course.objects.count()
    mappingcourses = FacultyCourseMapping.objects.all()
    fmcourses = []
    for course in mappingcourses:
        #print(type(course.faculty.facultyid))
        if(course.faculty.facultyid==int(fid)):
            fmcourses.append(course)
    print(fmcourses)
    dir(fmcourses)
    count=len(fmcourses)
    return render(request,"facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})
def facultychangepwd(request):
    fid = request.session["fid"]  # fid is session variable
    return render(request,"facultychangepwd.html", {"fid": fid})
def facultyupdatepwd(request):
    fid  = request.session["fid"]
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(fid,opwd,npwd)
    flag = Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))
    if flag:
        print("Old pwd is Correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        print("Updated....")
        msg = "Password Updated Successfully"
    else:
        print("Old pwd is Invalid")
        msg = "Old Password is Incorrect"
    return render(request,"facultychangepwd.html",{"fid":fid,"message":msg})