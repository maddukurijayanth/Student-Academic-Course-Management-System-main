from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
from django.http import HttpResponse
from django.shortcuts import  render





def demofunction(request):
    return HttpResponse("PFSD SDP PROJECT")
def demofunction1(request):
    return HttpResponse("<h3> KALASALINGAM UNIVERSITY</h3>")
def demofunction2(request):
    return HttpResponse("<font color='blue'>Student Academic Management System</font>")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def facultylogin(request):
    return render(request,"facultylogin.html ")

def studentlogin(request):
    return render(request,"studentlogin.html ")

def contactfunction(request):
    return render(request,"contact.html")
