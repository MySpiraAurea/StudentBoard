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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, NoteViewSet, ImageViewSet, ShapeViewSet, CommentViewSet
from .views import board_view

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'images', ImageViewSet)
router.register(r'shapes', ShapeViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('board/', board_view, name='board'),
]
