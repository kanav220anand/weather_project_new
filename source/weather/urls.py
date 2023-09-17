from django.urls import path
from weather.views import WeatherSearchView

app_name = 'weather'

urlpatterns = [
    path('search/', WeatherSearchView.as_view(), name='search'),
]
