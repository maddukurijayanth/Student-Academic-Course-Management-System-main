from django import forms
from .models import Faculty, Student


#AddFacultyForm will be created based on Faculty model

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty #model name
        fields = "__all__" # all fields in the model, auto field will be hided
        exclude = {"password"} #this will excluse fields
        labels = {"facultyid":"Enter Faculty ID","gender":"Select Gender","fullname":"Enter Full Name"} #you can change label names

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"password"}
        labels = {"studentid":"Enter student ID"}
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"studentid"}


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude = {"facultyid"}
