from django.urls import include, path
from rest_framework import routers
from . import views
from .views import VaccineUserRelationshipCreateView

router = routers.DefaultRouter()
router.register(r'vaccines', views.VaccineViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('participate_vaccine', VaccineUserRelationshipCreateView.as_view())
]