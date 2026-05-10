Student Academic Course Management System
This is a Django-based web application developed a Project.
The system is designed to manage academic course operations including student, faculty, and course
management using a 3-tier architecture (Frontend, Middleware, and Backend).
Technologies Used
- Frontend: HTML, CSS (Bootstrap), JavaScript
- Middleware: Django (Python Web Framework)
- Backend: PostgreSQL (via Django ORM)
Features
Authentication
- Admin, Faculty, and Student login
- Session management
- Password change functionality for all users
- CSRF protection
Student Module
- Login with session
- View profile
- Course registration (filtered by dept, year, sem, academic year)
- View mapped courses
- View course content
Faculty Module
- Login with session
- View profile
- View "My Courses" (Faculty-Course Mapping)
- Upload course content
- Change password
Admin Module
- Login with session
- Add / View / Update / Delete:
 - Students
 - Faculty
 - Courses
- Faculty-Course Mapping
- Change password
- Admin dashboard (statistics using object counts)
  
Project Setup

Step 1: Clone the Repository
git clone https://github.com/satyamukesh2004/Student-lms.git
cd Student-lms

Step 2: Set up Virtual Environment
python -m venv venv
venv\Scripts\activate (For Windows)

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Configure PostgreSQL in settings.py
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql',
 'NAME': 'smsproject',
 'USER': 'postgres',
 'PASSWORD': '<your_password>',
 'HOST': 'localhost',
 'PORT': '5432',
 }
}

Step 5: Run Migrations
python manage.py makemigrations
python manage.py migrate

Step 6: Create Superuser
python manage.py createsuperuser

Step 7: Run the Server
python manage.py runserver

Highlights
- Django Admin Console to manage backend operations
- PostgreSQL integration using Django ORM
- Session and cookie-based tracking for users
- CRUD operations via both forms and ModelForms
- Faculty-Course Mapping with ForeignKey and on_delete=models.CASCADE
- Bootstrap-based responsive design
- Modular code with separate apps: adminapp, studentapp, facultyapp
  
Topics Covered
- Django setup & project creation
- App creation (adminapp, studentapp, facultyapp)
- URL routing & views
- Template rendering and inheritance
- Static files and custom CSS/JS integration
- Model design using ORM
- Form handling (GET/POST, CSRF tokens)
- Django admin setup
- PostgreSQL configuration and migration
- Session management & login
- Faculty Course Mapping and content upload

