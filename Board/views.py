from rest_framework import viewsets
from .models import Board, Note, Image, Shape, Comment
from .serializers import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from .models import User, Student
from .forms import CustomUserCreationForm, logger
import logging


def board_view(request):
    return render(request, 'board.html')


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ShapeViewSet(viewsets.ModelViewSet):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class TheoryViewSet(viewsets.ModelViewSet):
    queryset = Theory.objects.all()
    serializer_class = TheorySerializer


def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'teacher':
            return redirect('teacher_sessions')
        elif request.user.role == 'student':
            return redirect('student_sessions')
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            logger.debug('Form is valid.')
            user = form.save()
            logger.debug(f'User {user} created.')
            login(request, user)
            return redirect('home')
        else:
            logger.debug('Form is not valid.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def teacher_sessions(request):
    return render(request, 'teacher/sessions.html')

@login_required
def teacher_timetable(request):
    return render(request, 'teacher/timetable.html')

@login_required
def teacher_students(request):
    return render(request, 'teacher/students.html')

@login_required
def teacher_balance(request):
    return render(request, 'teacher/balance.html')

@login_required
def student_sessions(request):
    return render(request, 'student/sessions.html')

@login_required
def student_timetable(request):
    return render(request, 'student/timetable.html')

@login_required
def student_homework(request):
    return render(request, 'student/homework.html')

@login_required
def student_theory(request):
    return render(request, 'student/theory.html')

