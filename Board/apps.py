from django.apps import AppConfig

class StudentBoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StudentBoard'

class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Board'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Users'
