from django.shortcuts import render
import requests

def index(request):
    api_key = '18065570bcc14b738d5dd9d2260968f9'
    current_weather_url = 'https://api.weatherbit.io/v2.0/current?city={}&key={}'
    forecast_url = 'https://api.weatherbit.io/v2.0/forecast/daily?city={}&key={}&days=7'

    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1 = fetch_weather(city1, api_key, current_weather_url)
        forecast_data1 = fetch_forecast(city1, api_key, forecast_url)

        if city2:
            weather_data2 = fetch_weather(city2, api_key, current_weather_url)
            forecast_data2 = fetch_forecast(city2, api_key, forecast_url)
        else:
            weather_data2 = None
            forecast_data2 = None

        context = {
            'weather_data1': weather_data1,
            'forecast_data1': forecast_data1,
            'weather_data2': weather_data2,
            'forecast_data2': forecast_data2,
        }

        return render(request, 'weather_app/index.html', context)
    else:
        return render(request, 'weather_app/index.html')

def fetch_weather(city, api_key, url):
    response = requests.get(url.format(city, api_key)).json()
    weather_data = {
        'city': city,
        'temperature': response['data'][0]['temp'],
        'description': response['data'][0]['weather']['description'],
        'icon': response['data'][0]['weather']['icon'],
    }
    return weather_data

def fetch_forecast(city, api_key, url):
    response = requests.get(url.format(city, api_key)).json()
    forecast_data = response['data']
    return forecast_data
