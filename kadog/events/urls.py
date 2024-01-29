from django.urls import include, path
from rest_framework import routers
from . import views
from .views import EventUserRelationshipCreateView

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('participate/', EventUserRelationshipCreateView.as_view())
]