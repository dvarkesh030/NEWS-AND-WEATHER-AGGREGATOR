from django.shortcuts import render
import requests
API_KEY_NEWS = 'd0b69496c18e463f888a273cb521ea9f'
API_KEY_WEATHER='aaba2d7cd73f453ca14144033222906'
CITY='TIRUCHIRAPPALLI'
CAT = 'Technology'
CAN = 'in'

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if category:
        url1=f'http://api.weatherapi.com/v1/current.json?key={API_KEY_WEATHER} &q={CITY}&aqi=no'
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY_NEWS}&country={CAN}'
        response = requests.get(url)
        response1 = requests.get(url1)
        data = response.json()
        data1 = response1.json()
        articles = data['articles']
    else:
        url1=f'http://api.weatherapi.com/v1/current.json?key={API_KEY_WEATHER} &q={CITY}&aqi=no'
        url = f'https://newsapi.org/v2/top-headlines?category={CAT}&apiKey={API_KEY_NEWS}&country={CAN}'
        response = requests.get(url)
        response1 = requests.get(url1)
        data = response.json()
        data1 = response1.json()
        articles = data['articles']

    weather = {
        'Name' :data1['location']['name'],
        'temp' :data1['current']['temp_c'],
        'description' : data1['current']['condition']['text'],
        'icon' :data1['current']['condition']['icon'],
    }
    context={
        'weather' : weather,
        'articles' :articles
    }

    return render(request, 'news_api/home.html', context)


