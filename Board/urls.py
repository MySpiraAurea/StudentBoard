"""
URL configuration for StudentBoard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'images', ImageViewSet)
router.register(r'shapes', ShapeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'homeworks', HomeworkViewSet)
router.register(r'theories', TheoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('teacher/sessions/', teacher_sessions, name='teacher_sessions'),
    path('teacher/timetable/', teacher_timetable, name='teacher_timetable'),
    path('teacher/students/', teacher_students, name='teacher_students'),
    path('teacher/balance/', teacher_balance, name='teacher_balance'),
    path('student/sessions/', student_sessions, name='student_sessions'),
    path('student/timetable/', student_timetable, name='student_timetable'),
    path('student/homework/', student_homework, name='student_homework'),
    path('student/theory/', student_theory, name='student_theory'),
    path('board/', board_view, name='board')
]
