from rest_framework import serializers
from .models import BoardUser, Lesson, Homework, Theory, Board, Note, Image, Shape, Comment

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    shapes = ShapeSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUser
        fields = ['id', 'username', 'email', 'role']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

class TheorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Theory
        fields = '__all__'

