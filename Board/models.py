from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

