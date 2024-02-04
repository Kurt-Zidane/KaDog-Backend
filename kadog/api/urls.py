from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('', include('vaccination.urls')),
]