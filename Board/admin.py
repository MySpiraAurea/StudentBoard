# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.html import format_html
from .models import BoardUser, Schedule


class BoardUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'role'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    class Media:
        css = {
            'all': (staticfiles_storage.url('css/admin.css'),)
        }

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student', 'subject', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('day_of_week', 'teacher', 'student')
    search_fields = ('teacher__username', 'student__username', 'subject')

admin.site.register(BoardUser, BoardUserAdmin)
admin.site.register(Schedule, ScheduleAdmin)