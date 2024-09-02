from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student
import logging

logger = logging.getLogger('StudentBoard')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            logger.debug(f'User {user} saved successfully.')
            student = Student.objects.create(
                user=user,
                email=user.email,
                username=user.username,
                password=user.password  # Сохраняем пароль в виде хэша
            )
            student.save()
            logger.debug(f'Student for user {user} created successfully.')
        else:
            logger.debug('User not saved because commit=False.')
        return user



