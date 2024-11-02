from django.shortcuts import render
import requests, datetime

def index(request):
    
    # if 'city' in request.POST:
    #     city = request.POST['city]']
    # else:
    #     city = 'Dhaka'
    
    appid = 'c943f9488856667dad61d556b893862b'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': 'japan', 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()
    return render(request, 'weatherapp/index.html',{'description': description, 'icon': icon, 'temp': temp, 'day': day})