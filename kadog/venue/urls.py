from django.urls import include, path
from rest_framework import routers
from .views import VenueListView, VenueDetailView,VenueEventListView, DogEventCreateView, DogEventListView,DogEventTotalView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', VenueListView.as_view()),
    path('total/', DogEventTotalView.as_view()),
    path('<int:pk>', VenueDetailView.as_view()),
    path('events/', VenueEventListView.as_view()),
    path('events/participants/',DogEventListView.as_view()),
    path('events/participate/',DogEventCreateView.as_view())
]