from django.contrib.auth.forms import AuthenticationForm
from rest_framework import viewsets
from .serializers import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import BoardUser
from .forms import CustomUserCreationForm, logger
from django.contrib import messages


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
    queryset = BoardUser.objects.all()
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
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            logger.debug('Form is not valid.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'teacher':
                    return redirect('teacher_sessions')
                elif user.role == 'student':
                    return redirect('student_sessions')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


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