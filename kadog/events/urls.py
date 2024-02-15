from django.urls import include, path
from rest_framework import routers
from .views import EventUserRelationshipCreateView, EventListView, EventDetailView, ParticipantListView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', EventListView.as_view()),
    path('<int:pk>/',EventDetailView.as_view()),
    path('participate/', EventUserRelationshipCreateView.as_view()),
    path('total/', ParticipantListView.as_view())
]