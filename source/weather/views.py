from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View
from app.weather_stack import WeatherStackUtils
from .models import SearchHistory

temp = {
    'request': {
        'type': 'City', 
        'query': 'New York, United States of America', 
        'language': 'en', 'unit': 'm'
    }, 
    'location': {
        'name': 'New York', 
        'country': 'United States of America', 
        'region': 'New York', 
        'lat': '40.714', 
        'lon': '-74.006', 
        'timezone_id': 'America/New_York', 
        'localtime': '2023-09-16 14:27', 
        'localtime_epoch': 1694874420, 
        'utc_offset': '-4.0'
    }, 
    'current': {
        'observation_time': '06:27 PM', 
        'temperature': 23, 
        'weather_code': 113, 
        'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 
        'weather_descriptions': ['Sunny'], 
        'wind_speed': 17, 
        'wind_degree': 290, 
        'wind_dir': 'WNW', 
        'pressure': 1013, 
        'precip': 0, 
        'humidity': 37, 
        'cloudcover': 0, 
        'feelslike': 24, 
        'uv_index': 5, 
        'visibility': 16, 
        'is_day': 'yes'
    }
}
from django import forms
from django.utils.translation import gettext_lazy as _
class CitySearchForm(forms.Form):
    city = forms.CharField(label=_('City'), max_length=30, required=False)

class WeatherSearchView(View):
    template_name = 'weather/index.html'
    # form_class = CitySearchForm
    
    def get(self, request):
        user = request.user
        query = self.request.GET.get('city')
        print("this is query", query)
        # resp = WeatherStackUtils.search_weather(query)
        resp = temp
        # print("RESPONSE", resp)
        weather_icon = resp.get("current").get("weather_icons")
        if weather_icon:
            weather_icon = weather_icon[0]
        else:
            weather_icon = ""
        weather = {
            "city": resp.get("location").get("name"),
            "country": resp.get("location").get("country"),
            "icon" : weather_icon,
            "temperature": resp.get("current").get("temperature"),
            "weather_descriptions" : resp.get("current").get("weather_descriptions"),
        }
        message = ''
        context = {'weather' : weather, 'message': message}

        SearchHistory.objects.create(user=user, keyword=query)
        return render(request, self.template_name, context) #returns the index.html template


