import urllib.request
from django.shortcuts import render
import urllib
import json

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        print(city)
        api_url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=7fa9d9d62e99f72bcf122157b80fb31d')
        load_url = json.load(api_url)
        print(load_url)

        data = {
            'city': city,
            'weather_description': load_url['weather'][0]['description'],
            'weather_icon': load_url['weather'][0]['icon'],
            'weather_temperature': load_url['main']['temp'],
            'weather_pressure': load_url['main']['pressure'],
            'weather_humidity': load_url['main']['humidity'],
        }

    else:
        data = {
            'city': None,
            'weather_description': None,
            'weather_icon':None,
            'weather_temperature': None,
            'weather_pressure': None,
            'weather_humidity': None,
        }
    return render(request, 'weatherapp/index.html', {'data':data})
