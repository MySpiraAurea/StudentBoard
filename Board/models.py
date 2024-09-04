# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('BoardUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class BoardUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class Note(models.Model):
    board = models.ForeignKey(Board, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Image(models.Model):
    board = models.ForeignKey(Board, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Shape(models.Model):
    board = models.ForeignKey(Board, related_name='shapes', on_delete=models.CASCADE)
    shape_type = models.CharField(max_length=50)  # Например, 'circle', 'square'
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=7)  # HEX-код цвета
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    note = models.ForeignKey(Note, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('BoardUser', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Lesson(models.Model):
    teacher = models.ForeignKey('BoardUser', related_name='lessons_as_teacher', on_delete=models.CASCADE)
    student = models.ForeignKey('BoardUser', related_name='lessons_as_student', on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.DurationField()

class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='homeworks', on_delete=models.CASCADE)
    file = models.FileField(upload_to='homework/')
    description = models.TextField()

class Theory(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



