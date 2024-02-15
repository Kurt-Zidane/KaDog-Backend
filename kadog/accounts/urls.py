from django.contrib import admin
from django.urls import path, include
from .views import CustomUserCurrentViewSet
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('users/me/', CustomUserCurrentViewSet.as_view({'get': 'retrieve'})),
]