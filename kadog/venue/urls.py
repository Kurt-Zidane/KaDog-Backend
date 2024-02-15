from django.urls import include, path
from rest_framework import routers
from .views import VenueListView, VenueDetailView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', VenueListView.as_view()),
    path('<int:pk>/',VenueDetailView.as_view()),
]