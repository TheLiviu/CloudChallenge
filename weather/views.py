from django.shortcuts import render

from django.urls import reverse_lazy
from django.http import JsonResponse
# Create your views here.
from django.views.generic.base import TemplateView
import requests

# Create your views here.
class HomeView(TemplateView):

  template_name = 'weather/home.html'
  success_url = reverse_lazy('home')







def weather_view(request):

  if request.method == 'GET' and 'lat' in request.GET and 'lon' in request.GET:
    lat = request.GET['lat']
    lon = request.GET['lon']
    api_key = 'a9a5df792641dd35267e193c1905901c'  # Replace with your OpenWeatherMap API key
    units = 'metric'
    lang = 'fr'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}&lang={lang}'
    response = requests.get(url)
 
    if response.status_code == 200:
      data = response.json()
      return JsonResponse(data)
    else:
      return JsonResponse({'error': 'Unable to fetch weather data'}, status=500)
  else:
    return JsonResponse({'error': 'Invalid request method or missing coordinates'}, status=400)

