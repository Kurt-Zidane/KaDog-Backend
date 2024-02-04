from django.urls import include, path
from rest_framework import routers
from .views import EventUserRelationshipCreateView, EventListView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', EventListView.as_view()),
    path('participate/', EventUserRelationshipCreateView.as_view())
]