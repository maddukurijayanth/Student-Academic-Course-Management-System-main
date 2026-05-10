from django.db import models
from django.db.models import Choices


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
            return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(HONORS)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)
    program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=50, blank=False, choices=program_choices)
    academic_choices = (("2024-25", "2024-25"), ("2023-24", "2023-24"))
    academicyear = models.CharField(max_length=20, blank=False,choices = academic_choices)
    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices = sem_choices)
    year = models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20, blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)
    ltps =  models.CharField(max_length=10,blank=False) #2-0-2-0
    credits = models.FloatField(blank = False)

    class Meta:
        db_table = "course_table"
    def __str__(self):
        return self.coursecode

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"))
    gender = models.CharField(max_length=20, blank=False,choices = gender_choices)
    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(HONORS)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=50, blank=False,choices = department_choices)
    program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=50, blank=False,choices = program_choices)
    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False, choices=sem_choices)
    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100, blank=False, default="klu123")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "student_table"
    def __str__(self):
        return str(self.studentid)


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"),("OTHERS","OTHERS"))
    gender = models.CharField(max_length=20, blank=False,choices = gender_choices)
    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(HONORS)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=50, blank=False,choices = department_choices)
    qualification_choices = (("M.Tech", "M.Tech"), ("Ph.D", "Ph.D"))
    qualification = models.CharField(max_length=50, blank=False,choices = qualification_choices)
    designation_choices = (("Prof.", "Professor"), ("Assoc. Prof.", "Associate Professor"), ("Asst. Prof", "Assistant Professor"))
    designation = models.CharField(max_length=50, blank=False,choices = designation_choices)
    password = models.CharField(max_length=100, blank=False, default="klu123")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "faculty_table"

    def __str__(self):
        return self.fullname
class FacultyCourseMapping(models.Model):
    mappingid = models.AutoField(primary_key=True)
    course  = models.ForeignKey(Course,on_delete=models.CASCADE) #course is an object of type Course
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE) #faculty is an object of type faculty
    component_choices = (("L","Lecture"),("T","Tutorial"),("P","Practical"),("S","Skilling"))
    component = models.CharField(max_length=10,blank=False,choices=component_choices)
    type = models.BooleanField(blank=False,verbose_name="Faculty Type(Main/Assistance)") #True means main Faculty, False means Assitance Faculty
    section = models.IntegerField(blank=False)
    class Meta:
        db_table = "facultycoursemapping_table"
    def __str__(self):
        return f"{self.course.coursetitle}--{self.faculty.fullname}"