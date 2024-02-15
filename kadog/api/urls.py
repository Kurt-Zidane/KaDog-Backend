from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('vaccines/', include('vaccination.urls')),
    path('', include('dogs.urls')),
    path('venues/', include('venue.urls'))
]