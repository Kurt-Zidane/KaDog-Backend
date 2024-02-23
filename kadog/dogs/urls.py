from django.urls import include, path
from rest_framework import routers
from .views import DogListCreateAPIView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('',),
    path('', DogListCreateAPIView.as_view()),
]