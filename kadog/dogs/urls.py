from django.urls import include, path
from rest_framework import routers
from .views import DogListCreateAPIView, DogDetailView, DogUpdateAPIView, DogRetrieveDestroyAPIView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('',),
    path('', DogListCreateAPIView.as_view()),
    path('detail/<int:pk>/', DogDetailView.as_view()),
    path('detail/<int:pk>/change/', DogUpdateAPIView.as_view()),
    path('detail/<int:pk>/delete/', DogRetrieveDestroyAPIView.as_view()),
]