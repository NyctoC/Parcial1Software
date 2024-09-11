from django.urls import path
from .views import HomePageView, flight_create
urlpatterns = [
 path('', HomePageView.as_view(), name='home'),
 path('create/', flight_create, name='flight_create'),
] 