from app.weather_stack import WeatherStackUtils
from django import forms
# Create your views here.
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import View
from weather.models import SearchHistory


class WeatherSearchView(View):
    template_name = 'weather/index.html'
    default_weather_data = {
        "city": "",
        "country": "",
        "icon" : "",
        "temperature": "",
        "weather_description" : "",
    }
    
    def get(self, request):
        user = request.user
        query = self.request.GET.get('city')
        resp = WeatherStackUtils.search_weather(query)

        success_resp =  resp.get("success")
        if success_resp is False:
            context = {'weather' : self.default_weather_data}
            SearchHistory.objects.create(user=user, keyword=query, found_result=False)
            return render(request, self.template_name, context)

        weather_icon = resp.get("current").get("weather_icons")
        if weather_icon:
            weather_icon = weather_icon[0]
        else:
            weather_icon = ""
        weather_description = resp.get("current").get("weather_descriptions")
        if weather_description:
            weather_description = weather_description[0]
        else:
            weather_description = ""

        weather = {
            "city": resp.get("location").get("name"),
            "country": resp.get("location").get("country"),
            "icon" : weather_icon,
            "temperature": resp.get("current").get("temperature"),
            "weather_description" : weather_description,
        }
        message = ''
        context = {'weather' : weather, 'message': message}

        SearchHistory.objects.create(user=user, keyword=query)
        return render(request, self.template_name, context) #returns the index.html template


