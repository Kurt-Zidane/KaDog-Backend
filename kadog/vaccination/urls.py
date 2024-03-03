from django.urls import path
from .views import VaccineUserRelationshipCreateView, VaccineListView, DogVaccineListView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', VaccineListView.as_view()),
    path('participate/', VaccineUserRelationshipCreateView.as_view()),
    path('participants/<int:vaccine_id>/', DogVaccineListView.as_view()),
]