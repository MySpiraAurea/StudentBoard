from rest_framework import serializers
from .models import Board, Note, Image, Shape, Comment

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

